import Vue from "vue";
import CustomerEntity from "../../domain/entities/Customer.entity";

let instance: ScheduleRegisterStore;

interface Props {
  open: boolean;
  date: string;
  hour: string;
  customer: CustomerEntity;
}

export default class ScheduleRegisterStore {
  store: Props = Vue.observable({
    open: false,
    date: "",
    hour: "",
    customer: new CustomerEntity(),
  });

  constructor() {
    if (!instance) {
      // eslint-disable-next-line @typescript-eslint/no-this-alias
      instance = this;
    }

    return instance;
  }

  open(handleDate: any) {
    console.log(`${handleDate}`, handleDate);
    this.store.date = `${handleDate.date}`;
    this.store.open = true;
  }

  close() {
    this.store.open = false;
  }
}
