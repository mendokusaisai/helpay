<template>
  <div class="helpay">
    <h1>This is an helpay page</h1>
    <CardsBoard />
  </div>
</template>

<script lang="ts">
import CardsBoard from "@/components/CardsBoard.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "HelpayView",
  components: {
    CardsBoard,
  },
});
</script>
