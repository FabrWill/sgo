import Http from "@/modules/http/Http";
import CustomerEntity from "../../domain/entities/Customer.entity";

interface CustomerLoadDTO {
  clientes: any[];
}

export default class CustomerLoadService extends Http {
  async load(): Promise<CustomerEntity[]> {
    const response = await this.get<CustomerLoadDTO>("/clientes");

    const validCustomers = response.clientes.filter(customer => {
      const birthdate = customer[2];

      console.log(birthdate);

      const hasAValidDate = birthdate ? birthdate.includes("-") : false;

      return hasAValidDate;
    });

    return validCustomers.map(cliente => {
      const [id, name, birthdate, cpf, civil_status, gender] = cliente;

      const customer = new CustomerEntity();

      customer.birthdate = birthdate;
      customer.id = id;
      customer.name = `${name}`;
      customer.cpf = cpf;
      customer.civil_status = civil_status;
      customer.gender = gender;

      return customer;
    });
  }
}
