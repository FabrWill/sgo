<template>
  <v-combobox
    v-model="model"
    :loading="loading"
    :items="items"
    outlined
    label="Nome do Cliente"
    item-text="name"
    @input="customerSelected"
  />
</template>

<script lang="ts">
import ModelManagement from "@/modules/shared/domain/model_management/ModelManagement.mixin";
import CustomerEntity from "@/modules/customer/domain/entities/Customer.entity";
import { mixins } from "vue-class-component";
import { Component } from "vue-property-decorator";
import CustomerService from "../../infra/http/CustomerLoad.service";

@Component({
  components: {},
})
class ScheduleRegisterModal extends mixins(ModelManagement) {
  items: CustomerEntity[] = [];
  loading = false;

  created() {
    this.search();
  }

  customerSelected() {
    if (this.model instanceof CustomerEntity) {
      console.log(this.model);
      this.$emit("selectedCustomer", this.model);
    }
  }

  async search() {
    try {
      this.loading = true;

      const clientes = await new CustomerService().load();

      this.items = clientes;
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
