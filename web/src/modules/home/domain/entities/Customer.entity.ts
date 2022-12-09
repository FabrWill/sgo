import ECivilStatus from "../enums/CivilStatus.enum";
import EGender from "../enums/Gender.enum";

export default class CustomerEntity {
  name = "";
  birthdate = "";
  cpf = "";
  civil_status = ECivilStatus.SOLTEIRO;
  gender = EGender.MALE;
}
