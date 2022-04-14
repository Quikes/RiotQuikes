<template>
  <v-snackbar
    v-model="show"
    :color="snackbar.color"
    outlined
    right
    timeout="2000"
  >
    {{ snackbar.text }}
    <template v-slot:action="{ attrs }">
      <v-btn color="blue" text v-bind="attrs" @click="$emit('clear')">
        Zamknij
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
export default {
  name: "CustomSnackbar",
  props: ["snackbar"],
  computed: {
    show() {
      return this.snackbar.open;
    },
  },
};
</script>

<style></style>
