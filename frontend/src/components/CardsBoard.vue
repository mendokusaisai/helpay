<template>
  <v-container>
    <v-btn v-on:click="save">保存</v-btn>
    <v-container>
      <v-row dense>
        <v-col v-for="member in members" :key="member.id" :cols="6">
          <v-card>
            <v-card-title>{{ member.name }}</v-card-title>
            <v-card-text> {{ member.point }} point </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-container>
      <v-row dense>
        <v-col v-for="card in cards" :key="card.name" :cols="6">
          <!--カード情報-->
          <v-card>
            <v-card-title>{{ card.name }}</v-card-title>
            <v-card-text>{{ card.point }} point</v-card-text>
            <v-divider></v-divider>
            <!-- ポイント付与ボタン -->
            <v-card-text>
              <v-chip-group column multiple v-model="selected[card.id]">
                <v-chip
                  v-for="member in members"
                  v-bind:key="member.name"
                  :active="member.id in card.targets"
                  :id="card.id + 'to' + member.id"
                  v-on:click="addPoint(member.id, card.id, card.point)"
                  filter
                  outlined
                >
                  {{ member.name }}
                </v-chip>
              </v-chip-group>
              <div>selected : {{ selected[card.id] }}</div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "vue";
import { Card, Member } from "../interface";

export default defineComponent({
  name: "CardsBoard",
  data() {
    return {
      cards: Array<Card>(),
      members: Array<Member>(),
      selected: {},
    };
  },
  mounted() {
    axios.get("/api/cards/").then((response) => {
      this.cards = response["data"];
    });
    axios.get("/api/members/").then((response) => {
      this.members = response["data"];
    });
    let o: { [key: number]: [] };
    o = {};
    for (var c of this.cards) {
      o[c.id] = [];
    }
    this.selected = o;
  },
  methods: {
    addPoint: function (memberId: number, cardId: number, cardPoint: number) {
      const button = document.getElementById(
        cardId.toString() + "to" + memberId.toString()
      );
      if (button) {
        if (button.getAttribute("class") == "pushed") {
          button.setAttribute("class", "");
          for (var m1 of this.members) {
            if (m1.id == memberId) {
              m1.point -= cardPoint;
            }
          }
        } else {
          button.setAttribute("class", "pushed");
          for (var m2 of this.members) {
            if (m2.id == memberId) {
              m2.point += cardPoint;
            }
          }
        }
      }
    },
    save: function () {
      axios.post("api/members/save/", this.members).then((response) => {
        console.log(response.data);
      });
      var buttons = document.getElementsByClassName("pushed");
      var elements = Array.from(buttons);
      elements.forEach((x) => x.setAttribute("class", ""));
    },
  },
});
</script>
