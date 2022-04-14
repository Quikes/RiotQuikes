import axios from "axios";
import Cookies from "js-cookie";

// axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
// axios.defaults.xsrfCookieName = "csrftoken";
// axios.defaults.withCredentials = true;

export const api = axios.create({
  baseURL: "api/v1/",
  withCredentials: true,
  headers: {
    "Access-Control-Allow-Headers": "*",
    "Content-Type": "application/json",
    "X-CSRFToken": Cookies.get("csrftoken"),
  },
});
