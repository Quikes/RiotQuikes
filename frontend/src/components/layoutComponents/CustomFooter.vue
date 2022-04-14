<template>
  <div class="footerStyle">
    <v-footer color="background">
      <v-row justify="center" no-gutters>
        <!-- <v-btn
          variant="text"
          class="mx-2"
          rounded="xl"
          @click="goTo('/regulamin')"
        >
          Regulamin serwisu
        </v-btn>
        <v-btn
          variant="text"
          class="mx-2"
          rounded="xl"
          @click="goTo('/polityka')"
        >
          Polityka prywatności
        </v-btn> -->
        <v-col class="text-right mr-4">
          QuikeSoft ©{{ new Date().getFullYear() }}
        </v-col>
      </v-row>
    </v-footer>
  </div>
</template>

<script>
export default {
  name: "CustomFooter",
  methods: {
    goTo(link) {
      this.$router.push(link);
    },
  },
};
</script>

<style lang="scss" scoped>
.footerStyle {
  position: absolute;
  bottom: 0;
  width: 100%;
  button,
  div {
    color: grey;
    font-size: 0.8rem;
  }
}
</style>
