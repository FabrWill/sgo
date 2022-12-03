import {
  Grid,
  Container,
  AppBar,
  Toolbar,
  IconButton,
  Typography,
  Button,
} from "@mui/material";
import { Link } from "react-router-dom";
import "./landing.page.css";

interface Props {}

const LandingPage: React.FC<Props> = ({}) => {
  return (
    <div className="page">
      <AppBar position="static" elevation={0} color="transparent">
        <Toolbar variant="dense">
          <Button
            href="/home"
            variant="text"
            size="small"
            color="success"
            sx={{ ml: "auto" }}
          >
            <Typography
              variant="overline"
              color="inherit"
              component="div"
              sx={{ color: "rgba(0, 0, 0, 0.82)", fontWeight: 700 }}
            >
              Acesse
            </Typography>
          </Button>
        </Toolbar>
      </AppBar>
      <Grid container spacing={2} className="h-100">
        <Grid item xs={12} className="d-flex flex-row align-center">
          <h1 className="landing-title mx-auto">SGO</h1>
        </Grid>
      </Grid>
      <Grid container className=" d-flex flex-row">
        <Grid item xs={12} className="mx-auto d-flex flex-item flex-column">
          <p className="landing-span w-100">O único capaz de ajudar</p>
          <p className="w-100">
            <b>sua clínica</b>
            <br /> <b> você</b>
            <br /> <b> Seu Cliente</b>
            <br /> <b> Seu Financeiro</b>
            <br /> <b> E Muito Mais</b>
          </p>
        </Grid>
      </Grid>
    </div>
  );
};

export default LandingPage;
