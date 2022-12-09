import CustomerEntity from "@/modules/customer/domain/entities/Customer.entity";
import ServiceEntity from "@/modules/services/domain/entities/Services.entity";
import Vue from "vue";
import ScheduleEntity from "../../domain/entities/Schedule.entity";
import ScheduleSaveService from "../../infra/http/ScheduleSave.service";

let instance: ScheduleRegisterStore;

interface Props extends ScheduleEntity {
  open: boolean;
}

export default class ScheduleRegisterStore {
  store: Props = Vue.observable({
    id: 0,
    open: false,
    date: "",
    hour: "",
    customer: new CustomerEntity(),
    service: new ServiceEntity(),
  });

  constructor() {
    if (!instance) {
      // eslint-disable-next-line @typescript-eslint/no-this-alias
      instance = this;
    }

    return instance;
  }

  async save() {
    const result = await new ScheduleSaveService().save(this.store);

    console.log(result);
  }

  open(handleDate: any) {
    this.store.date = `${handleDate.date}`;
    this.store.open = true;
  }

  close() {
    this.store.open = false;
  }
}
