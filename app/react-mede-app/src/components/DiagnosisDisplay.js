import React, { useEffect, useState } from 'react';
import { List, Header, Container } from "semantic-ui-react"

export const DiagnosisDisplay = ({ features }) => {
    console.log(features);
    console.log(features.length);

    // Fetch diagnosis from Python (features already posted and processed)
    const [diagnosis, setDiagnosis] = useState("");
    console.log("init", diagnosis);

    fetch('/tester').then(response =>
        response.json().then(data => {
            setDiagnosis(data.diagnosis);
        }));
    console.log("diagnosis", diagnosis);

    // Only display diagnosis if features have been submitted
    if (features.length <= 0) {
        return (<Container />);
    }

    return (
        <Container>
            <Header as='h2' block={true} >
                <Header.Content>
                    Diagnosis Result:
                    <Header.Subheader>{diagnosis}</Header.Subheader>
                </Header.Content>
            </Header>
        </Container>
    )
}