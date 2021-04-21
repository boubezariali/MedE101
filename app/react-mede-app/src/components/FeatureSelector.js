// Handles rendering clinical features
import React, { useState } from 'react';
import { Dropdown, Form, Button } from "semantic-ui-react"

const options = [
    { key: 'heart_attack', text: "Heart Attack", value: 'heart_attack' },
    { key: "stroke", text: "Stroke", value: 'stroke' },
    { key: "asthma", text: "Asthma", value: "asthma" }
]

export const FeatureSelector = ({ onNewFeature }) => {
    const [features, setFeatures] = useState(options);
    return (
        <Form>
            <Form.Field>
                <Dropdown
                    placeholder='Input Clinical Feature'
                    fluid
                    search
                    selection
                    multiple
                    options={options}
                    onChange={
                        (event, data) => setFeatures(data.value)
                    }
                />
            </Form.Field>
            <Form.Field>
                <Button onClick={async () => {
                    const response = await fetch('/add_feature', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(features)
                    })

                    if (response.ok) {
                        console.log("response ok");
                        console.log(features);
                    }
                }}
                >Submit</Button>
            </Form.Field>
        </Form>
    )
}