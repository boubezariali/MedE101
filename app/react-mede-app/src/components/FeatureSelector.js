// Handles rendering clinical features
import React, { useState } from 'react';
import { List, Header, Dropdown, Form, Button } from "semantic-ui-react"

const options = [
    { key: 'heart_attack', text: "Heart Attack", value: 'heart_attack' },
    { key: "stroke", text: "Stroke", value: 'stroke' },
    { key: "asthma", text: "Asthma", value: "asthma" }
]
export const FeatureSelector = ({ onNewFeature }) => {
    const [feature, setFeature] = useState('');
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
                />
            </Form.Field>
            <Form.Field>
                <Button onClick={async () => {
                    const response = await fetch('/add_feature', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(feature)
                    })

                    if (response.ok) {
                        console.log("response ok");
                        onNewFeature(feature)
                    }
                }}
                >Submit</Button>
            </Form.Field>
        </Form>
    )
}