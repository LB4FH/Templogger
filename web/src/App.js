import './App.css';
import Data from './SampleData.json';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        Temperature: {Data.last[0].Temperature} °C <br />
        Humidity: {Data.last[0].Humidity} % <br />
        Last read: {Data.last[0].Timestamp} 
      </header>
    </div>
  );
}


export default App;
