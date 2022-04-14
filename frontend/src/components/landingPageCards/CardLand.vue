<template>
  <div class="cardAdv" style="position: relative">
    <div class="circleClass mx-auto pt-1" :style="'background-color:' + color">
      {{ num }}
    </div>
    <div class="text-center ma-6 mt-8">
      <h5 class="font-weight-regular pt-12" v-html="message"></h5>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardLAnd",
  props: ["message", "num", "color"],
};
</script>

<style lang="scss" scoped>
$base-color3: #44a3b2;
$base-color1: #1f7690;
$base-color2: #3591a4;
$base-color4: #55b6c1;
$base-color5: #6acfd3;

.circleClass {
  font-size: 1.5rem;
  color: white;
  font-weight: bold;
  border: 4px solid white;
  box-shadow: 0px 0px 5px #888888;
  //   background-color: #44a3b2;
  border-radius: 50px;
  width: 50px;
  height: 50px;
  text-align: center;
  margin: auto;
  position: relative;
  position: absolute;
  margin-top: -20px;
  margin-right: auto;
  width: 50px;
  left: calc(50% - 25px);
}
</style>
