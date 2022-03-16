<template>
  <div>
    <v-expansion-panels>
      <v-expansion-panel
        v-for="(item, i) in tiers"
        :key="i"
        :title="item.name"
        :text="JSON.stringify(item)"
        @click="fetchTier(item.id)"
      >
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
import { toRaw } from "vue";
import { retrieveData } from "../utils/api.js";
export default {
  name: "TierList",
  data() {
    return {
      tiers: [],
    };
  },
  methods: {
    async fetchTiersList() {
      this.tiers = await retrieveData(`tiersList`);
    },
    async fetchTier(id) {
      const tier = await retrieveData(`tiers/${id}`);
      this.tiers = this.tiers.map((item) =>
        toRaw(item).id === id ? tier : item
      );
    },
  },
  mounted() {
    this.fetchTiersList();
  },
};
</script>

<style lang="scss" scoped></style>
