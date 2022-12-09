<template>
  <v-container fill-height>
    <v-sheet height="100%" width="100%">
      <v-calendar
        ref="calendar"
        v-model="value"
        type="month"
        :events="events"
        :event-overlap-threshold="30"
        @click:date="openRegisterModal"
      ></v-calendar>

      <schedule-register-modal />
    </v-sheet>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import ScheduleService from "../../infra/http/ScheduleLoad.service";
import ScheduleRegisterStore from "../stores/ScheduleRegister.store";
import ScheduleRegisterModal from "../components/ScheduleRegisterModal.vue";

export default Vue.extend({
  name: "HomeView",
  components: {
    ScheduleRegisterModal,
  },
  data: () => ({
    weekday: [0, 1, 2, 3, 4, 5, 6],
    value: "",
    events: [],
    scheduleRegister: new ScheduleRegisterStore(),
  }),
  async created() {
    const result = await new ScheduleService().load();

    console.log("result", result);
  },
  methods: {
    openRegisterModal(date: Date) {
      this.scheduleRegister.open(date);
    },
  },
});
</script>
