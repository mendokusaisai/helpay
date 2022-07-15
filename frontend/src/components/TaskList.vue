<template>
  <v-container fluid>
    <p>{{ isOpenDialog }}</p>
    <v-dialog v-model="dialog" width="500">
      <DepositDialog v-on:clickDeposit="onDeposit" />
    </v-dialog>
    <v-switch
      v-model="multiSelectMode"
      label="複数選択"
      @change="changeMultiSelect"
    />
    <v-btn v-if="multiSelectMode" @click="openDepositDialog">決定</v-btn>

    <v-card max-width="475" class="mx-auto">
      <v-list subheader flat dense>
        <v-subheader>手伝いリスト</v-subheader>
        <v-list-item-group multiple v-model="selectedTaskIds">
          <v-list-item
            v-for="card in cards"
            :key="card.id"
            :value="card.id"
            @click="openDepositDialogList"
          >
            <template v-slot:default="{ active }">
              <v-list-item-action v-if="multiSelectMode">
                <v-checkbox :input-value="active" color="primary"></v-checkbox>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>{{ card.name }}</v-list-item-title>
                <v-list-item-subtitle>{{ card.point }}pt</v-list-item-subtitle>
              </v-list-item-content>
            </template>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "vue";
import { Card } from "../interface";
import DepositDialog from "./dialogs/DepositDialog.vue";
export default defineComponent({
  name: "TaskList",
  props: {
    msg: String,
  },
  components: {
    DepositDialog,
  },
  data() {
    return {
      cards: Array<Card>(),
      selectedTaskIds: [],

      // taskList関連
      multiSelectMode: false,
      dialog: false,
    };
  },
  mounted() {
    axios.get("/api/cards/").then((response) => {
      this.cards = response["data"];
      console.log(this.cards);
    });
  },
  methods: {
    changeMultiSelect: function () {
      this.selectedTaskIds = [];
    },
    openDepositDialog: function () {
      this.dialog = true;
    },
    openDepositDialogList: function () {
      if (this.multiSelectMode == false) {
        this.dialog = true;
      }
    },
    onDeposit() {
      this.dialog = false;
    },
  },
});
</script>
