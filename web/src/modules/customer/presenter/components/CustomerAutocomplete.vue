<template>
  <v-combobox
    v-model="model"
    :loading="loading"
    :items="items"
    outlined
    label="Nome do Cliente"
  />
</template>

<script lang="ts">
import ModelManagement from "@/modules/shared/domain/model_management/ModelManagement.mixin";
import ISelectItem from "@/modules/shared/domain/vuetify/SelectItem";
import { mixins } from "vue-class-component";
import { Component, Vue } from "vue-property-decorator";

@Component({
  components: {},
})
class ScheduleRegisterModal extends mixins(ModelManagement) {
  items: ISelectItem[] = [];
  loading = false;

  created() {
    this.search();
  }

  search() {
    try {
      this.loading = true;
    } catch (error) {
      console.error(error);
    }
  }
}

export default ScheduleRegisterModal;
</script>

<style></style>
