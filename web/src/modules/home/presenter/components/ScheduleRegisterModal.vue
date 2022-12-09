<template>
  <v-dialog v-model="state.store.open" width="1200">
    <v-card>
      <v-card-title> Cadastrar Agendamentos </v-card-title>

      <v-card-text>
        <v-form>
          <v-container fluid>
            <v-row>
              <v-col sm="3" xs="12">
                <date-picker
                  v-model="state.store.date"
                  label="Data de atendimento"
                />
              </v-col>
              <v-col sm="3" xs="12">
                <time-picker
                  v-model="state.store.hour"
                  label="Horário de Atendimento"
                />
              </v-col>
            </v-row>
            <v-divider class="my-3" />
            <v-row>
              <v-col sm="3" xs="12">
                <service-autocomplete
                  v-model="state.store.service.name"
                  @serviceSelected="selectService"
                />
              </v-col>
              <v-col sm="3" xs="12">
                <v-text-field-money
                  v-model="state.store.service.value"
                  :properties="{ outlined: true, locale: 'pt-BR' }"
                  label="Preço"
                />
              </v-col>
            </v-row>
            <v-divider class="my-3" />
            <v-row>
              <v-col sm="3" xs="12">
                <customer-autocomplete
                  v-model="state.store.customer.name"
                  @selectedCustomer="selectedCustomer"
                />
              </v-col>

              <v-col sm="3" xs="12">
                <v-text-field-cpf
                  v-model="state.store.customer.cpf"
                  label="CPF"
                  :properties="{ outlined: true }"
                  required
                />
              </v-col>

              <v-col sm="3" xs="12">
                <date-picker
                  v-model="state.store.customer.birthdate"
                  label="Data de Nascimento"
                />
              </v-col>

              <v-col sm="3" xs="12">
                <v-select
                  v-model="state.store.customer.gender"
                  :items="genderItems"
                  outlined
                  label="Sexo"
                  required
                />
              </v-col>

              <v-col sm="3" xs="12">
                <v-select
                  v-model="state.store.customer.civil_status"
                  :items="civilStatusItems"
                  outlined
                  label="Estado Civil"
                  required
                />
              </v-col>
            </v-row>
          </v-container>
        </v-form>
      </v-card-text>

      <v-divider />

      <v-card-actions>
        <v-container>
          <v-row>
            <v-spacer />
            <v-btn outlined color="primary" @click="save" :loading="loading">
              Salvar
            </v-btn>
          </v-row>
        </v-container>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import ScheduleRegisterStore from "../stores/ScheduleRegister.store";
import DatePicker from "@/modules/shared/components/datepicker/DatePicker.vue";
import ISelectItem from "@/modules/shared/domain/vuetify/SelectItem";
import EGender from "../../domain/enums/Gender.enum";
import ECivilStatus from "../../domain/enums/CivilStatus.enum";
import TimePicker from "@/modules/shared/components/datepicker/TimePicker.vue";
import CustomerAutocomplete from "@/modules/customer/presenter/components/CustomerAutocomplete.vue";
import CustomerEntity from "@/modules/customer/domain/entities/Customer.entity";
import ServiceAutocomplete from "@/modules/services/presenter/components/ServiceAutocomplete.vue";
import ServiceEntity from "@/modules/services/domain/entities/Services.entity";

@Component({
  components: {
    CustomerAutocomplete,
    ServiceAutocomplete,
    DatePicker,
    TimePicker,
  },
})
class ScheduleRegisterModal extends Vue {
  state = new ScheduleRegisterStore();
  loading = false;

  genderItems: ISelectItem[] = [
    { text: "Masculino", value: EGender.MALE },
    { text: "Feminino", value: EGender.FEMALE },
  ];

  civilStatusItems: ISelectItem[] = [
    { text: "Solteiro", value: ECivilStatus.SOLTEIRO },
    { text: "Casado", value: ECivilStatus.VIUVO },
    { text: "Viúvo", value: ECivilStatus.CASADO },
  ];

  selectedCustomer(customer: CustomerEntity) {
    this.state.store.customer.id = customer.id;
    this.state.store.customer.name = customer.name;
    this.state.store.customer.birthdate = customer.birthdate;
    this.state.store.customer.cpf = customer.cpf;
    this.state.store.customer.civil_status = customer.civil_status;
    this.state.store.customer.gender = customer.gender;
  }

  selectService(service: ServiceEntity) {
    this.state.store.service.name = service.name;
    this.state.store.service.value = service.value;
    this.state.store.service.id = service.id;
  }

  async save() {
    try {
      this.loading = true;

      console.log("salve", this.state);

      await this.state.save();
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
