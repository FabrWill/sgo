import { observer } from "mobx-react-lite";
import React from "react";
import { ScheduleDialogStore } from "./ScheduleDialog.store";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  Divider,
  TextField,
  Grid,
  Select,
  MenuItem,
} from "@mui/material";
import { TimePicker, DesktopDatePicker } from "@mui/x-date-pickers";
import { GrowTransition } from "../../../../../shared/navigation/GrodAnimation";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { AdapterLuxon } from "@mui/x-date-pickers/AdapterLuxon";
import { DateTime } from "luxon";
import CPFField from "../../../../../shared/formik/cpf/CPFField";
import Schedule from "../../../domain/entities/Schedule.entity";
import { useFormik } from "formik";
import { ptBR } from "@mui/x-date-pickers/locales";

interface Props {
  store: ScheduleDialogStore;
}

const ScheduleDialog: React.FC<Props> = observer(({ store }) => {
  const formik = useFormik<Schedule>({
    initialValues: {
      ...new Schedule(),
    },
    onSubmit: () => {}
  });

  return (
    <form onSubmit={formik.handleSubmit}>
    <LocalizationProvider
      dateAdapter={AdapterLuxon}
      localeText={ptBR as any}
    >
      <Dialog
        open={store.isOpen}
        onClose={() => store.close()}
        TransitionComponent={GrowTransition}
        maxWidth="lg"
        fullWidth={true}
      >
        <DialogTitle sx={{ fontFamily: "Raleway" }}>Agendamentos</DialogTitle>
        <Divider />
        <DialogContent>
          <Grid container spacing={2}>
            <Grid item xs={12} md={3}>
              <TimePicker
                label="Data do Agendamento"
                value={store.schedule}
                onChange={(date: DateTime, event: any) =>
                  store.changeDate(date)
                }
                views={["hours"]}
                shouldDisableTime={(timeValue: any, clockType: any) => {
                  if (
                    (clockType === "hours" && timeValue < 8) ||
                    timeValue == 12 ||
                    timeValue > 17
                  ) {
                    return true;
                  }

                  return false;
                }}
                ampm={false}
                renderInput={(params) => <TextField {...params} fullWidth/>}
              />
            </Grid>
            <Grid item xs={12} md={9} />
            <Divider/>
            <Grid item xs={12} md={4}>
              <CPFField 
                label="CPF*"
                name="CPF"
                formik={formik}
                fullWidth
              />
            </Grid>
            <Grid item xs={12} md={4}>
              <TextField
                label="Nome"
                variant="outlined"
                fullWidth
              />
            </Grid>
            <Grid item xs={12} md={4}>
              <DesktopDatePicker
                value={store.birthdate}
                label="Data de Nascimento"
                onChange={store.changeDate}
                renderInput={(params) => (
                  <TextField {...params} fullWidth />
                )}
              />
            </Grid>

            <Grid item xs={12} md={4}>
              <TextField
                label="Estado Civil"
                variant="outlined"
                fullWidth
                select
              >
                <MenuItem value={"S"}>Solteiro</MenuItem>
                <MenuItem value={"C"}>Casado</MenuItem>
                <MenuItem value={"V"}>Viúvo</MenuItem>
              </TextField>
            </Grid>

            <Grid item xs={12} md={4}>
              <TextField label="Sexo" variant="outlined" fullWidth select>
                <MenuItem value={"M"}>Masculino</MenuItem>
                <MenuItem value={"F"}>Feminino</MenuItem>
              </TextField>
            </Grid>
          </Grid>
        </DialogContent>
      </Dialog>
    </LocalizationProvider>
    </form>
  );
});

export default ScheduleDialog;
