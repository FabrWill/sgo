import { observer } from "mobx-react-lite";
import React from "react";
import { ScheduleDialogStore } from "./ScheduleDialog.store";
import { Dialog, DialogTitle, DialogContent, Divider } from "@mui/material";
import { GrowTransition } from "../../../../../shared/navigation/GrodAnimation";

interface Props {
  store: ScheduleDialogStore;
}

const ScheduleDialog: React.FC<Props> = observer(({ store }) => {
  return (
    <Dialog
      open={store.isOpen}
      onClose={() => store.close()}
      TransitionComponent={GrowTransition}
      maxWidth="lg"
      fullWidth={true}
    >
      <DialogTitle sx={{fontFamily: "Raleway"}}>Agendamentos</DialogTitle>
      <Divider />
      <DialogContent>teste som</DialogContent>
    </Dialog>
  );
});

export default ScheduleDialog;
