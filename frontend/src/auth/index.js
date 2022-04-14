/* eslint-disable no-console */
import router from "../router";
// import Cookies from "js-cookie";

import Axios from "axios";
const API_URL = process.env.VUE_APP_API_ENDPOINT;
const LOGIN_URL = API_URL + "token/";
const USER_URL = API_URL + "users/";

export default {
  user: {
    authenticated: false,
  },

  login(context, creds) {
    Axios.post(LOGIN_URL, creds).then(
      (response) => {
        localStorage.setItem("token", response.data.access);
        localStorage.setItem("tokenRefresh", response.data.refresh);
        Axios.defaults.headers.common["Authorization"] =
          "JWT " + localStorage.getItem("token");
        this.getAuthHeader();
        this.getUserInfo(creds);
        router.push("/import");
      },
      (error) => {
        alert("Niepoprawny email lub hasło!");
        console.log(error);
      }
    );
  },
  logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("tokenRefresh");
    this.user.authenticated = false;
    Axios.defaults.headers.common["Authorization"] = "";
    router.push("/");
  },

  checkAuth() {
    var jwt = localStorage.getItem("token");
    if (jwt) {
      this.user.authenticated = true;
    } else {
      this.user.authenticated = false;
    }
    return this.user.authenticated;
  },
  // The object to be passed as a header for authenticated requests
  getAuthHeader() {
    console.log("'Authorization': 'JWT '" + localStorage.getItem("token"));
    return {
      Authorization: "JWT " + localStorage.getItem("token"),
    };
  },
  getUserInfo(creds) {
    Axios.get(USER_URL, { params: creds }).then((response) => {
      console.log(response.data);
    });
  },
};
