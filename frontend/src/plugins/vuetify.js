// Styles
import "@mdi/font/css/materialdesignicons.css";
import "vuetify/styles";

// Vuetify
import { createVuetify } from "vuetify";
import colors from "vuetify/lib/util/colors";

export default createVuetify({
  theme: {
    defaultTheme: "dark",
    themes: {
      light: {
        dark: false,
        colors: {
          primary: "#17728d",
          secondary: colors.red.lighten4,
          background: "white",
        },
      },
      dark: {
        dark: true,
        colors: {
          primary: "#17728d",
          secondary: colors.red.lighten4,
          background: "blue",
        },
      },
    },
  },
});
// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
