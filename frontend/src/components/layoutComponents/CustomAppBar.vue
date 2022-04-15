<template>
  <v-card class="navbar">
    <v-layout>
      <v-app-bar color="primary" density="compact">
        <v-app-bar-title>Riot Api Testing</v-app-bar-title>
        <template v-slot:append>
          <v-btn icon="mdi-account-circle" @click="goTo('/profile')"></v-btn>
        </template>
      </v-app-bar>

      <v-main> </v-main>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: "CustomAppBar",
  methods: {
    goTo(link) {
      this.$router.push(link);
    },
  },
};
</script>

<style lang="scss" scoped>
.navbar {
  top: 0;
  width: 100%;
  button,
  div {
    color: rgb(255, 255, 255);
    font-size: 1.5rem;
  }
}
</style>
