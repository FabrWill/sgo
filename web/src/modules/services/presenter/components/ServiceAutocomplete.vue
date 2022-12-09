<template>
  <v-autocomplete
    v-model="model"
    :loading="loading"
    :items="items"
    outlined
    label="Servico"
    item-text="name"
    @input="serviceSelected"
    return-object
  />
</template>

<script lang="ts">
import ModelManagement from "@/modules/shared/domain/model_management/ModelManagement.mixin";
import { mixins } from "vue-class-component";
import { Component } from "vue-property-decorator";
import ServiceEntity from "../../domain/entities/Services.entity";
import ServiceLoadService from "../../infra/http/ServiceLoad.service";

@Component({
  components: {},
})
class ScheduleRegisterModal extends mixins(ModelManagement) {
  items: ServiceEntity[] = [
    ServiceEntity.build({ id: 0, name: "Clínica Geral", value: 150 }),
    ServiceEntity.build({ id: 0, name: "Clareamento", value: 250 }),
    ServiceEntity.build({ id: 0, name: "Tratamento de Canal", value: 350 }),
    ServiceEntity.build({ id: 0, name: "Implante Dentário", value: 500 }),
  ];
  loading = false;

  created() {
    this.search();
  }

  serviceSelected() {
    console.log("update\n", this.model, this.model instanceof ServiceEntity);
    if (this.model instanceof ServiceEntity) {
      this.$emit("serviceSelected", this.model);
    }
  }

  async search() {
    try {
      this.loading = true;

      const services = await new ServiceLoadService().load();

      this.items = services;
    } catch (error) {
      console.error(error);
    } finally {
      this.loading = false;
    }
  }
}

export default ScheduleRegisterModal;
</script>

<style></style>
