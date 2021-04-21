import React, { useEffect, useState } from 'react';
import { Container, Header } from 'semantic-ui-react';
import './App.css';
import { ClinicalFeatures } from './components/ClinicalFeatures';
import { FeatureSelector } from './components/FeatureSelector';


function App() {
  const [features, setFeatures] = useState([]);
  useEffect(() => {
    fetch('/tester').then(response =>
      response.json().then(data => {
        setFeatures(data.test_items);
      }));
  }, [])

  return (
    <div className="App">
      <Container style={{ marginTop: 40 }}>
        <Header as='h2' block={true}>
          <Header.Content>
            Differential Diagnosis Trainer
            <Header.Subheader>Input clinical features and submit for diagnosis</Header.Subheader>
          </Header.Content>
        </Header>
        
        <FeatureSelector/>

        <ClinicalFeatures features={features} />
      </Container>
    </div>
  );
}

export default App;
