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
                <v-text-field
                  v-model="state.store.service.description"
                  outlined
                  label="Serviço"
                />
              </v-col>
              <v-col sm="3" xs="12">
                <v-text-field-money
                  v-model="state.store.service.price"
                  :properties="{ outlined: true, locale: 'pt-BR' }"
                  label="Preço"
                />
              </v-col>
            </v-row>
            <v-divider class="my-3" />
            <v-row>
              <v-col sm="3" xs="12">
                <customer-autocomplete v-model="state.store.customer.name" />
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
            <v-btn outlined color="primary"> Salvar </v-btn>
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

@Component({
  components: {
    CustomerAutocomplete,
    DatePicker,
    TimePicker,
  },
})
class ScheduleRegisterModal extends Vue {
  state = new ScheduleRegisterStore();

  genderItems: ISelectItem[] = [
    { text: "Masculino", value: EGender.MALE },
    { text: "Feminino", value: EGender.FEMALE },
  ];

  civilStatusItems: ISelectItem[] = [
    { text: "Solteiro", value: ECivilStatus.SOLTEIRO },
    { text: "Casado", value: ECivilStatus.VIUVO },
    { text: "Viúvo", value: ECivilStatus.CASADO },
  ];
}

export default ScheduleRegisterModal;
</script>

<style></style>
