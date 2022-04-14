import axios from "axios";
import Cookies from "js-cookie";

export default axios.create({
  baseURL: process.env.VUE_APP_API_ENDPOINT2,
  timeout: 300000,
  headers: {
    "Content-Type": "application/json",
    "X-CSRFToken": Cookies.get("csrftoken"),
    JWT: localStorage.getItem("token"),
  },
});
