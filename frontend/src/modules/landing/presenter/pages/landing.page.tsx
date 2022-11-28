import { Grid, Container } from "@mui/material";
import "./landing.page.css";

interface Props {}

const LandingPage: React.FC<Props> = ({}) => {
  return (
    <Container maxWidth="xl" className="page">
      <Grid container spacing={2} className="h-100">
        <Grid item xs={12} className="d-flex flex-row align-center">
          <h1 className="landing-title mx-auto">SGO</h1>
        </Grid>
      </Grid>
      <Grid container className=" d-flex flex-row">
        <Grid item xs={12} className="mx-auto d-flex flex-item flex-column">
        <p className="landing-span w-100">
                O único capaz de ajudar</p>
          <p className="w-100">
           <b>sua clínica</b>
                                <br/> <b> você</b>
                                <br/> <b> Seu Cliente</b>
                                <br/> <b> Seu Financeiro</b>
                                <br/> <b> E Muito Mais</b>
          </p>
        </Grid>
      </Grid>
    </Container>
  );
};

export default LandingPage;
