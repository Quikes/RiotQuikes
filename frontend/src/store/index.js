import { createStore } from "vuex";
import currentUser from "./modules/currentUser";

export default createStore({
  // state: {},
  // getters: {},
  // mutations: {},
  // actions: {},
  modules: {
    currentUser,
  },
});
