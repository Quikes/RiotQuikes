<template>
  <div id="login">
    <div class="mb-10"><slot /></div>
    <custom-footer />
  </div>
</template>

<script>
import CustomFooter from "./components/layoutComponents/CustomFooter.vue";

export default {
  name: "loginLayout",
  components: { CustomFooter },
};
</script>

<style></style>
s
