/*diagnosisPage.jsx*/
import React, { useState } from 'react';
import { Container, Header, Card } from 'semantic-ui-react';
import { DiagnosisDisplay } from '../components/DiagnosisDisplay';
import { FeatureSelector } from '../components/FeatureSelector';

const DiagnosisPage = () => {
  const [features, setFeatures] = useState([]);

  return (
    <div >
      <Container style={{ marginTop: 40, marginBottom: 80 }}>
        <Card centered={true} fluid={true}>
          <Card.Content header={"Differential Diagnosis Helper"} />
          <Card.Content>
            Search for and select clinical features from the dropdown below. Submit for diagnosis.
          </Card.Content>
        </Card>

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
export default DiagnosisPage;