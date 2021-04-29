/*home.jsx*/
import React from "react";
import { Container, Card, Button } from 'semantic-ui-react';

const GamePage = () => {
    return (
        <Container style={{ marginTop: 40, marginBottom: 80 }}>
            <Card centered={true} fluid={true}>
                <Card.Content header={"Game Mode"} />
                <Card.Content>
                    <Card.Description>
                        Practice your diagnosis skills with this game. Currently in development.
                        </Card.Description>
                </Card.Content>
                <Card.Content extra>
                    <Button>Start game!</Button>
                </Card.Content>
            </Card>
        </Container>
    );
};

export default GamePage;