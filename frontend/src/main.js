import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import { loadFonts } from "./plugins/webfontloader";
loadFonts();

import LoginLayout from "./LoginLayout";
import DefLayout from "./DefLayout";
import MainLayout from "./MainLayout";
import setup from "../interceptors";

// wtyczki do komponentów
import Datepicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";

const app = createApp(App).use(router).use(store).use(vuetify);
setup();

app.component("DefLayout", DefLayout);
app.component("LoginLayout", LoginLayout);
app.component("MainLayout", MainLayout);

app.component("DatePicker", Datepicker);

app.mount("#app");
