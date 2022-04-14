<template>
  <v-btn color="primary" variant="outlined" @click="getTemplateTemp()">
    Pobierz szablon pliku
  </v-btn>
</template>

<script>
import axios from "axios";

export default {
  name: "TemplateButton",
  methods: {
    getTemplate() {
      axios({
        method: "get",
        url: process.env.VUE_APP_API_ENDPOINT2 + `template/`,
        responseType: "blob",
      })
        .then((response) => {
          let fileURL = window.URL.createObjectURL(new Blob([response.data]));
          var fileLink = document.createElement("a");
          fileLink.href = fileURL;
          fileLink.setAttribute("download", "Szablon Raport Kadr.pdf");
          document.body.appendChild(fileLink);
          fileLink.click();
        })
        .catch(() => {
          this.$emit("showMessage", {
            open: true,
            text: "Wystąpił błąd przy pobieraniu",
            color: "accent-4",
          });
          console.log("error occured");
        });
    },
    async getTemplateTemp() {
      try {
        let anchor = document.createElement("a");
        anchor.href = process.env.VUE_APP_API_ENDPOINT2 + `media/szablon.xlsx`;
        anchor.download = `raportKadr_szablon.xlsx`;
        document.body.appendChild(anchor);
        await anchor.click();
      } catch (err) {
        console.log("error");
      }
    },
  },
};
</script>

<style></style>
