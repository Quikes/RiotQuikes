<template>
  <div>
    <custom-app-bar />
    <div>
      <div><slot /></div>
    </div>

    <custom-footer />
  </div>
</template>

<script>
import CustomFooter from "./components/layoutComponents/CustomFooter.vue";
// import CustomDrawer from "./components/layoutComponents/CustomDrawer.vue";
import CustomAppBar from "./components/layoutComponents/CustomAppBar.vue";

export default {
  name: "loginLayout",
  components: { CustomFooter, CustomAppBar },
};
</script>

<style></style>
