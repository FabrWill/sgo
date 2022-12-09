<template>
  <v-menu
    ref="menu"
    v-model="menu"
    :close-on-content-click="false"
    :nudge-right="40"
    transition="scale-transition"
    offset-y
    max-width="290px"
    min-width="290px"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-text-field
        v-model="formattedHour"
        :label="label"
        prepend-inner-icon="mdi-clock-time-four-outline"
        readonly
        outlined
        v-bind="attrs"
        v-on="on"
      ></v-text-field>
    </template>
    <v-time-picker
      v-if="menu"
      v-model="model"
      :allowed-hours="validTime"
      :allowed-minutes="() => false"
      full-width
      format="24hr"
      @click:hour="saveTime"
    ></v-time-picker>
  </v-menu>
</template>

<script lang="ts">
import { mixins } from "vue-class-component";
import { Component, Prop } from "vue-property-decorator";
import ModelManagement from "../../domain/model_management/ModelManagement.mixin";

@Component({})
class TimePicker extends mixins(ModelManagement) {
  menu = false;

  @Prop()
  label?: string;

  saveTime(time: any) {
    const timePicker: any = this.$refs.menu;

    if (!timePicker) {
      return;
    }

    console.log(time);

    timePicker.save(time);

    this.model = `${time}:00`;
  }

  get formattedHour() {
    console.log(this.model);

    if (!this.model) {
      return "00:00";
    }

    const hour = Number.parseInt(this.model.split(":")[0]);

    return `${this.model} às ${hour + 1}:00`;
  }

  validTime(time: number) {
    if (time >= 8 && time < 12) {
      return true;
    }

    if (time >= 13 && time < 17) {
      return true;
    }

    return false;
  }
}

export default TimePicker;
</script>

<style></style>
