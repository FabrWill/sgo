import ECivilStatus from "../../../home/domain/enums/CivilStatus.enum";
import EGender from "../../../home/domain/enums/Gender.enum";

export default class CustomerEntity {
  name = "";
  birthdate = "";
  cpf = "";
  civil_status = ECivilStatus.SOLTEIRO;
  gender = EGender.MALE;
}
