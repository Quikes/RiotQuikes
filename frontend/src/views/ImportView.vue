<template>
  <div>
    <v-card elevation="1" class="ma-16 mt-md-16 mr-md-16 mr-2 ml-md-16 ml-24">
      <v-progress-linear
        v-if="loading"
        class="position-absolute"
        style="z-index: 1"
        color="primary"
        height="3"
        indeterminate
      />
      <v-card-title>Import danych</v-card-title>
      <v-card-text>
        Zakładka pozwalająca na import pliku w formacie .xls lub .xlsx oraz
        pobranie jego szablonu. Po wgraniu załącznika podlega on walidacji i
        zwracana jest informacja o nieprawidłowych wartościach.
        <v-container class="grey lighten-5">
          <v-row align="start">
            <v-col xs="12" sm="12" md="3" lg="3" xl="2">
              <date-picker
                v-model="date"
                monthPicker
                class="mt-3 datePickerPrimary"
                locale="pl"
              />
            </v-col>
            <v-col xs="12" sm="12" md="6" lg="6" xl="8">
              <v-file-input
                label="Wybierz plik"
                v-model="file"
                accept=".xls,.xlsx"
              />
            </v-col>
            <v-col xs="12" sm="12" md="3" lg="3" xl="2">
              <v-btn
                color="primary"
                variant="outlined"
                @click="uploadFile()"
                class="mt-3"
              >
                Wyślij do walidacji
              </v-btn>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <template-button @showMessage="updateSnackbar" />
      </v-card-actions>
    </v-card>
    <custom-snackbar :snackbar="snackbar" @clear="updateSnackbar" />

    <v-dialog v-model="errorReportDialog" scrollable width="80vw">
      <v-card>
        <v-card-title>Raport błędów</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="max-height: 80vh">
          <div
            v-for="(item, i) in formattedErrorReport"
            :key="'error_' + i"
            v-html="item"
            class="mb-4"
          />
          <div v-if="formattedErrorReport == 0">Nie wykryto błędów</div>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn
            color="primary"
            text
            @click="exportErrors()"
            v-if="formattedErrorReport != 0"
          >
            Pobierz raport błędów
          </v-btn>
          <v-btn color="primary" text @click="errorReportDialog = false">
            Zamknij
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import TemplateButton from "../components/importModule/TemplateButton.vue";
import CustomSnackbar from "../components/layoutComponents/CustomSnackbar.vue";
import { mapState } from "vuex";
import api from "../services/api";
import { saveAs } from "file-saver";

export default {
  name: "HomeView",
  data() {
    return {
      snackbar: {
        open: false,
        text: "",
        color: "",
      },
      date: {
        month: new Date().getMonth(), //you need to add 1 before sending
        year: new Date().getFullYear(),
      },
      file: [],
      errorReport: [],
      errorReportDialog: false,
      loading: false,
    };
  },
  methods: {
    updateSnackbar(
      msg = {
        open: false,
        text: "",
        color: "",
      }
    ) {
      this.snackbar = msg;
    },
    uploadFile() {
      this.loading = true;
      let dataDict = {
        file: this.file[0],
        year: this.date.year,
        month: this.date.month + 1,
        user_id: this.currentUser.id,
        company: this.currentUser.company,
      };
      let dataToSend = new FormData();
      Object.entries(dataDict).forEach(([key, value]) => {
        dataToSend.append(key, value);
      });

      api
        .post(`fileupload/`, dataToSend)
        .then((response) => {
          api
            .get(`fileupload/${response.data.id}/filechecker/`)
            .then((res) => {
              this.loading = false;
              this.errorReport = res.data;
              this.errorReportDialog = true;
              this.file = [];
            })
            .catch((err) => {
              this.loading = false;
              this.updateSnackbar({
                open: true,
                text: "Wystąpił błąd przy walidacji pliku.",
                color: "accent-4",
              });
              console.log(err.status, " ---- ", err.data);
            });
        })
        .catch((error) => {
          this.loading = false;
          // const errorMsg = error.data.file.join(" ") || ''
          const errorMsg = error.data.file.join(" ")
            ? error.data.file.join(" ")
            : "";
          this.updateSnackbar({
            open: true,
            text: "Wystąpił błąd przy imporcie. " + errorMsg,
            color: "accent-4",
          });
          console.log(error.status, " ---- ", error.data);
        });
    },
    exportErrors() {
      var XLSX = require("xlsx");
      const fileType =
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8";
      const fileExtension = ".xlsx";
      const ws = XLSX.utils.json_to_sheet(
        [
          {
            desc: "OPIS BŁĘDU",
            sheet_name: "NAZWA ARKUSZA",
            column_name: "NAZWA KOLUMNY",
            row_number: "NAZWA WIERSZA",
            false_val: "NIEPRAWIDŁOWA WARTOŚĆ",
            true_val: "OCZEKIWANA WARTOŚĆ",
          },
        ].concat(this.errorReport),
        {
          header: [
            "desc",
            "sheet_name",
            "column_name",
            "row_number",
            "false_val",
            "true_val",
          ],
          skipHeader: true,
          // sheet: "Sheet JS",
          // raw: true,
        }
      );
      const wb = { Sheets: { data: ws }, SheetNames: ["data"] };
      const excelBuffer = XLSX.write(wb, { bookType: "xlsx", type: "array" });
      const data = new Blob([excelBuffer], { type: fileType });
      saveAs(data, "Raport błędów" + fileExtension);
    },
    s2ab(s) {
      var buf = new ArrayBuffer(s.length);
      var view = new Uint8Array(buf);
      for (var i = 0; i < s.length; i++) view[i] = s.charCodeAt(i) & 0xff;
      return buf;
    },
  },
  computed: {
    ...mapState({
      currentUser: (state) => state.currentUser.currentUser,
    }),
    formattedErrorReport() {
      return this.errorReport.map((item) => {
        let msg = `W arkuszu o nazwie <strong>${item.sheet_name}</strong> wystąpił błąd <strong>${item.desc}</strong>. Nieprawidłowa wartość`;
        if (item.false_val) msg += ` <strong>${item.false_val}</strong>`;
        if (item.column_name)
          msg += ` w kolumnie <strong>${item.column_name}</strong>`;
        if (item.row_number)
          msg += ` w wierszu <strong>${item.row_number}</strong>`;
        if (item.true_val)
          msg += ` powinna być zastąpiona <strong>${item.true_val}</strong>`;
        return msg + ".";
      });
    },
  },
  components: {
    TemplateButton,
    CustomSnackbar,
  },
};
</script>

<style lang="scss" scoped></style>
