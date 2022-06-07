<template>
  <div class="menbers_list">
    <button v-on:click="addMember">追加</button>
    <button v-on:click="saveMembers">保存</button>
    <ul>
      <li v-for="member in members" v-bind:key="member.id">
        <div>
          <p>{{ member.name }}</p>
          <p>{{ member.point }}point</p>
          <div>
            name:
            <input name="name" type="text" v-model="member.name" />
          </div>
          <div>
            point:
            <input name="point" type="number" v-model="member.point" />
          </div>
          <button v-on:click="deleteMember(member.id)">削除</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "vue";
import { Member } from "../interface";

export default defineComponent({
  name: "MembersList",
  data() {
    return {
      members: Array<Member>(),
    };
  },
  mounted() {
    axios.get("/api/members/").then((response) => {
      this.members = response["data"];
    });
  },
  methods: {
    addMember: function () {
      axios.get("api/members/new/").then((response) => {
        this.members.push(response["data"]);
      });
      axios.get("/api/members/").then((response) => {
        this.members = response["data"];
        console.log(this.members);
      });
    },
    deleteMember: function (target_id: number) {
      console.log(this.members);
      console.log(target_id);
      const data = { id: target_id.toFixed() };
      axios.post("api/members/delete/", data).then((response) => {
        console.log(response.data);
      });
      axios.get("/api/members/").then((response) => {
        this.members = response["data"];
        console.log(this.members);
      });
    },
    saveMembers: function () {
      axios.post("api/members/save/", this.members).then((response) => {
        console.log(response.data);
      });
    },
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
