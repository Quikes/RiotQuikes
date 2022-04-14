import api from "@/services/api";
import router from "@/router";
import axios from "axios";

// let counter = 0;

export default function setup() {
  api.interceptors.request.use(
    function (config) {
      let source = axios["CancelToken"].source();
      const token = localStorage.getItem("token");
      config.cancelToken = source.token;
      if (token) {
        config.headers.Authorization = `JWT ${token}`;
      }
      return config;
    },
    function (err) {
      return Promise.reject(err);
    }
  );
  let counter = 0;
  api.interceptors.response.use(
    (response) => {
      counter += 1;
      console.log(counter);

      if (counter > 10 && localStorage.getItem("token")) {
        counter = 0;
        console.log(counter);
        api
          .post("token/refresh/", {
            refresh: localStorage.getItem("tokenRefresh"),
          })
          .then((response) => {
            localStorage.setItem("token", response.data.access);
            // localStorage.setItem("tokenRefresh", response.data.refresh);
            api.defaults.headers.common["Authorization"] =
              "JWT " + localStorage.getItem("token");
          });
      }
      return response;
    },
    (err) => {
      const {
        response: { status, data },
      } = err;

      if (status == 401) {
        localStorage.removeItem("token");
        localStorage.removeItem("tokenRefresh");
        router.go();
      }

      if (status == 407) {
        localStorage.removeItem("token");
        localStorage.removeItem("tokenRefresh");
        router.go();
        return null;
      }
      if (data.detail == "Signature has expired.") {
        localStorage.removeItem("token");
        localStorage.removeItem("tokenRefresh");
        router.go();
      } else {
        console.log(data);
      }
      throw err.response;
    }
  );
}
