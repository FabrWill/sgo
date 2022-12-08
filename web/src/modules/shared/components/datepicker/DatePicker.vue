<template>
  <v-menu
    v-model="menu"
    :close-on-content-click="false"
    :nudge-right="40"
    transition="scale-transition"
    offset-y
    min-width="auto"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-text-field
        v-model="formattedDate"
        :label="label"
        prepend-inner-icon="mdi-calendar"
        readonly
        outlined
        v-bind="attrs"
        v-on="on"
      ></v-text-field>
    </template>
    <v-date-picker v-model="model" @input="menu = false"></v-date-picker>
  </v-menu>
</template>

<script lang="ts">
import { mixins } from "vue-class-component";
import { Component, Prop } from "vue-property-decorator";
import ModelManagement from "@/modules/shared/domain/model_management/ModelManagement.mixin";

@Component({})
class DatePicker extends mixins(ModelManagement) {
  @Prop()
  label?: string;

  menu = false;

  get formattedDate() {
    if (!this.model) return null;

    const [year, month, day] = this.model.split("-");

    return `${day}/${month}/${year}`;
  }
}

export default DatePicker;
</script>

<style></style>
