<template>
  <dv-container class="cards">
    <CardsList />
  </dv-container>
</template>

<script lang="ts">
import CardsList from "@/components/CardsList.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "CardsView",
  components: {
    CardsList,
  },
});
</script>
