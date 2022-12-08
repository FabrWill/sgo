import { Vue, Prop, Watch } from "vue-property-decorator";
import Component from "vue-class-component";

@Component
class ModelManagement extends Vue {
  @Prop({ required: true })
  value: any;

  model: any = null;

  @Watch("model")
  emitInputEvent() {
    this.$emit("input", this.model);
    this.$emit("changed", this.model);
  }

  @Watch("value")
  updateModelValue() {
    this.model = this.value;
  }

  mounted() {
    this.model = this.value;
  }
}

export default ModelManagement;
