import Vue from "vue";
import CustomerEntity from "../../../customer/domain/entities/Customer.entity";
import ServiceEntity from "../../domain/entities/Service.entity";

let instance: ScheduleRegisterStore;

interface Props {
  open: boolean;
  date: string;
  hour: string;
  customer: CustomerEntity;
  service: ServiceEntity;
}

export default class ScheduleRegisterStore {
  store: Props = Vue.observable({
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

  open(handleDate: any) {
    this.store.date = `${handleDate.date}`;
    this.store.open = true;
  }

  close() {
    this.store.open = false;
  }
}
