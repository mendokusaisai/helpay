<template>
  <div class="cards">
    <h1>This is an cards page</h1>
    <CardsList />
  </div>
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
