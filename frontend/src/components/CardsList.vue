<template>
  <!-- カード一覧 -->
  <v-container>
    <!-- 追加ボタン -->
    <v-btn v-on:click="addCard">追加</v-btn>
    <v-btn v-on:click="saveCards">保存</v-btn>
    <v-container>
      <v-row dense>
        <v-col dense v-for="card in cards" v-bind:key="card.id" :cols="3">
          <!--カード情報-->
          <v-card>
            <v-simple-table>
              <tbody>
                <tr>
                  <td>
                    <v-text-field v-model="card.name" />
                  </td>
                  <td>
                    <v-text-field v-model="card.point" />
                  </td>
                </tr>
              </tbody>
            </v-simple-table>

            <!-- 削除ボタン
            <v-card-actions>
              <v-btn v-on:click="deleteCard(card.id)">削除</v-btn>
            </v-card-actions>-->
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-list>
      <v-list-item v-for="file in files" :key="file.title">
        <v-list-item-avatar>
          <v-icon :class="file.color" dark v-text="file.icon"></v-icon>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title v-text="file.title"></v-list-item-title>

          <v-list-item-subtitle v-text="file.subtitle"></v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-action>
          <v-btn icon>
            <v-icon color="grey lighten-1">mdi-information</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
    </v-list>
  </v-container>
</template>

<script lang="ts">
export interface CardPayload {
  id: number;
  name: string;
  point: number;
  targets: Array<number>;
}

import axios from "axios";
import { defineComponent } from "vue";
import { Card, Member } from "../interface";

export default defineComponent({
  name: "CardsList",
  props: {
    msg: String,
  },
  data() {
    return {
      cards: Array<Card>(),
      members: Array<Member>(),
    };
  },
  mounted() {
    axios.get("/api/cards/").then((response) => {
      this.cards = response["data"];
      console.log(this.cards);
    });

    axios.get("/api/members/").then((response) => {
      this.members = response["data"];
    });
    console.log(this.cards);
  },
  methods: {
    addCard: function () {
      axios.get("api/cards/new/").then((response) => {
        this.cards.push(response["data"]);
      });
      axios.get("/api/cards/").then((response) => {
        this.cards = response["data"];
        console.log(this.cards);
      });
    },
    deleteCard: function (target_id: number) {
      console.log(this.cards);
      console.log(target_id);
      const data = { id: target_id.toFixed() };
      axios.post("api/cards/delete/", data).then((response) => {
        console.log(response.data);
      });
      axios.get("/api/cards/").then((response) => {
        this.cards = response["data"];
        console.log(this.cards);
      });
    },
    saveCards: function () {
      var payload: CardPayload[] = [];
      this.cards.forEach((element: Card) => {
        payload.push({
          id: element["id"],
          name: element["name"],
          point: element["point"],
          targets: element["targets"],
        });
      });
      axios.post("api/cards/save/", payload).then((response) => {
        console.log(response.data);
      });
    },
  },
});
</script>
