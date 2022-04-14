<template>
  <div class="mb-15">
    <h5 class="text-center font-weight-regular">
      Monitorowanie wartości wynagrodzeń pracowników<br />
      jako najistotniejszego kosztu związanego z działalnością podmiotów
      leczniczych
    </h5>
    <h2 class="text-center ma-5 font-weight-regular">
      appRKP (Raport Kadrowo-Płacowy)
    </h2>
    <div class="text-center ma-auto">
      <v-btn
        v-if="false"
        class="px-10 shadow gradientAotmit"
        text
        @click="goTo('/logowanie')"
      >
        Logowanie
      </v-btn>
    </div>
    <div class="text-center ma-auto gridDisp mt-10">
      <div
        class="blockCard"
        style="justify-self: end"
        @click="getTemplateTemp(`szablon.xlsx`)"
      >
        <img
          :src="require('../assets/ikonka_pobierz_szablon_pliku_cropped.svg')"
          style="width: 28px"
          class="mt-2"
        /><br />
        <p class="font-weight-regular" style="font-size: 12px">
          pobierz szablon pliku
        </p>
      </div>
      <div
        class="blockCard"
        @click="getTemplateTemp('INSTRUKCJA-RAPORT-KADROWO-PŁACOWY.pdf')"
      >
        <img
          :src="require('../assets/ikonka_pobierz_instrukcję_cropped.svg')"
          style="width: 40px"
          class="mt-2"
        /><br />
        <p class="font-weight-regular" style="font-size: 12px">
          pobierz instrukcję
        </p>
      </div>
    </div>
    <!-- <template-button @showMessage="updateSnackbar" /> -->
    <div class="text-center ma-auto mt-16" style="width: 30%">
      <v-row>
        <v-col>
          <img
            :src="require('../assets/ikonka_wprowadzanie_danych-cropped.svg')"
            style="width: 40px"
            class="mt-2"
          />
          <h4 class="text-center ma-5 font-weight-regular">
            Wprowadzanie danych
          </h4>
          <h5 class="text-center ma-10 font-weight-regular">
            Tutaj wprowadzisz i zatwierdzisz dane płacowo-kadrowe dotyczące
            pracowników zatrudnionych w&nbsp;Twoim podmiocie
          </h5>
        </v-col>
        <v-col>
          <img
            :src="require('../assets/ikonka_raporty-cropped.svg')"
            style="width: 40px"
            class="mt-2"
          />
          <h4 class="text-center ma-5 font-weight-regular">Raporty</h4>
          <h5 class="text-center ma-10 mx-15 font-weight-regular">
            Tutaj wygererujesz w&nbsp;formie tabel i&nbsp;wykresów według
            wybranych przez siebie kryteriów
          </h5>
        </v-col>
      </v-row>
    </div>
    <div class="text-center ma-auto">
      <v-btn
        class="px-10 shadow gradientAotmit"
        style="
          width: 55%;
          text-transform: none;
          font-weight: bold;
          cursor: default;
        "
        >Korzyści z użytkowania aplikacji
      </v-btn>
    </div>
    <div class="marginCards">
      <v-row>
        <v-col>
          <card-land :message="message[0]" :num="1" color="#1f7690"></card-land>
          <!-- <div class="cardAdv" style="position: relative">
            <div class="circleClass mx-auto pt-1">1</div>
            <div class="text-center ma-6 mt-8">
              <h5 class="font-weight-regular pt-12">
                Automatyzacja procesu przekazywania danych finansowo-kadrowych -
                wprowadzenie danych przez import udostępnionego szablonu plików
              </h5>
            </div>
          </div> -->
        </v-col>
        <v-col>
          <card-land
            :message="message[1]"
            :num="2"
            color="#1f7690;"
          ></card-land>
        </v-col>
        <v-col>
          <card-land
            :message="message[2]"
            :num="3"
            color="#44a3b2;"
          ></card-land>
        </v-col>
        <v-col>
          <card-land :message="message[3]" :num="4" color="#55b6c1"></card-land>
        </v-col>
        <v-col>
          <card-land
            :message="message[4]"
            :num="5"
            color="#6acfd3;"
          ></card-land>
        </v-col>
      </v-row>
    </div>
    <custom-snackbar :snackbar="snackbar" @clear="updateSnackbar" />
  </div>
</template>

<script>
import router from "../router";
import CustomSnackbar from "../components/layoutComponents/CustomSnackbar.vue";
import CardLand from "../components/landingPageCards/CardLand.vue";

export default {
  name: "LandingPage",
  components: {
    CustomSnackbar,
    CardLand,
  },
  data() {
    return {
      snackbar: {
        open: false,
        text: "",
        color: "",
      },
      message: [
        "Automatyzacja procesu przekazywania danych finansowo-kadrowych - wprowadzenie danych przez import udostępnionego szablonu plików",
        "Monitorowanie dynamiki zmian kosztów osobowych pracowników w&nbsppodziale na kategorie personelu i&nbspformę zatrudnienia",
        "Reprezentatywna proba danych pozwoli na rzetelne oszacowanie taryf",
        "Prezentacja wyników w postaci zbiorczych raportów&nbspi analiz przekrojowych ",
        "Docelowa możliwość benchmarkingui&nbspna podstawie zanonimizowanych danych innych podmiotów w podziale na kategorie personelu i&nbspwojewództwa ",
      ],
    };
  },
  methods: {
    goTo(link) {
      router.push(link);
    },
    updateSnackbar(
      msg = {
        open: false,
        text: "",
        color: "",
      }
    ) {
      this.snackbar = msg;
    },
    async getTemplateTemp(name) {
      try {
        let anchor = document.createElement("a");
        anchor.target = "_blank";
        anchor.href = process.env.VUE_APP_API_ENDPOINT2 + `media/${name}`;
        anchor.download = name;
        document.body.appendChild(anchor);
        await anchor.click();
      } catch (err) {
        console.log("error");
      }
    },
  },
};
</script>

<style scoped>
.shadow {
  box-shadow: 0px 0px 5px #afafaf;
  border: 3px solid white;
  border-radius: 10px;
}
.gridDisp {
  width: 22%;
  display: grid;
  grid-template-columns: repeat(2, auto);
  grid-column-gap: 25px;
}
.blockCard {
  height: 90px;
  border-radius: 12px;
  box-shadow: 0px 0px 5px #888888;
  background-color: white;
  cursor: pointer;
  width: 150px;
}
.cardAdv {
  min-height: 240px;
  border-radius: 12px;
  box-shadow: 0px 0px 5px #888888;
}
.marginCards {
  margin: 40px 240px 0px 240px;
}

.gradientAotmit {
  color: white;
  background: #207790;
  background: -webkit-linear-gradient(left, #207790, #6ad0d3);
  background: -moz-linear-gradient(left, #207790, #6ad0d3);
  background: linear-gradient(to right, #207790, #6ad0d3);
}
</style>
