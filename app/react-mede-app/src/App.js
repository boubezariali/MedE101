import React, { useState } from 'react';
import { Container, Header } from 'semantic-ui-react';
import './App.css';
import { DiagnosisDisplay } from './components/DiagnosisDisplay';
import { FeatureSelector } from './components/FeatureSelector';

function App() {
  const [features, setFeatures] = useState([]);

  return (
    <div className="App">
      <Container style={{ marginTop: 40, marginBottom: 80 }}>
        <Header as='h2' block={true}>
          <Header.Content>
            Differential Diagnosis Trainer
            <Header.Subheader>Input clinical features and submit for diagnosis</Header.Subheader>
          </Header.Content>
        </Header>

        <FeatureSelector
          onNewFeatures={newFeatures => setFeatures(newFeatures)}
        />
      </Container>

      <Container>
        <DiagnosisDisplay features={features} />
      </Container>
    </div>
  );
}

export default App;
