const Greet: React.FC<{ name: string }> = ({ name }) => <h1>Hello, {name}!</h1>;

const App: React.FC = () => <Greet name="World" />;
