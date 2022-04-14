<template>
  <v-app>
    <v-main>
      <div id="content" style="min-height: 100vh">
        <component :is="layout"><router-view /></component>
      </div>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({}),
  computed: {
    layout() {
      return this.$route.meta.layout || "DefLayout";
    },
  },
};
</script>
<style lang="scss">
body,
button {
  font-family: "Montserrat", "Helvetica Neue", Arial, sans-serif !important;
}

.dp__theme_light {
  --dp-primary-color: #17728d !important;
  --dp-success-color: #17728d !important;
}
h4,
h5 {
  line-height: 1.6em;
}
</style>
