import CustomerEntity from "@/modules/customer/domain/entities/Customer.entity";
import ServiceEntity from "@/modules/services/domain/entities/Services.entity";

export default class ScheduleEntity {
  id = 0;
  date = "2022-12-09";
  hour = "08:00";
  customer: CustomerEntity = new CustomerEntity();
  service: ServiceEntity = new ServiceEntity();
}
