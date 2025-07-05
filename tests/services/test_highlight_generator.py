from app.services.highlight_generator import HighlightGeneratorAgent

agent = HighlightGeneratorAgent()


def test_highlight_generation(generator=agent):
    stories = [
        """It had been nearly a decade since Emily had stepped foot in her grandparents’ old mountain cabin. Overgrown weeds lined the stone path, and ivy curled lazily around the faded wooden porch. Stepping inside, the air smelled of dust and pine; scattered were old board games, a chipped mug her grandfather always used, and a sun-bleached photograph of her family smiling one summer long ago.
        Driven by nostalgia, Emily spent the afternoon cleaning and exploring. She traced her fingers over carvings in the wooden beams—initials and dates from childhood summers, each marking a memory of late-night ghost stories and burnt marshmallows. As dusk fell, she lit the old fireplace, the crackling flames casting dancing shadows that felt almost alive.
        While rummaging through a drawer, Emily discovered an envelope addressed to her in her grandmother’s delicate handwriting. Inside was a short letter: words of love, hope, and the gentle reminder that even when places change, the memories built there remain untouched. Reading it, tears blurred Emily’s vision, yet her heart felt lighter, anchored in something both lost and beautifully found.
        That night, she stepped outside onto the porch. The mountains stood silent under a sky teeming with stars, and for the first time in years, she felt like she’d come home.""",
        """It began as a small idea on a rainy afternoon: turning the empty patch of yard behind the house into a shared garden. Maya convinced her younger brother Leo to help, and together they spent weekends digging, planting, and learning the language of soil and sunlight. Their hands became rough from work, but each sprout that broke the earth felt like magic.
        By midsummer, the garden was alive with color—sunflowers stretching high, tomatoes blushing red, and lavender swaying gently in the breeze. Neighbors stopped by to admire their work, sometimes offering advice, sometimes just smiling at the sight of two kids building something so patiently. Maya and Leo, once quick to argue over anything, found themselves laughing over stubborn weeds and racing to spot the first blossom.
        One evening, as fireflies lit up the twilight, they sat side by side on the garden bench they had built from old wood. The scent of earth and flowers mingled with the warm air, and Maya realized they had grown something far more precious than vegetables: a shared memory that would bloom every summer in their hearts.""",
        """Raj had planned for a quiet summer: books, lazy mornings, and maybe the occasional swim. But life, it seemed, had other ideas. It began when his childhood friend Maya showed up unannounced, car keys in hand and an infectious grin that dared him to say no.
        Their days became a whirlwind of unplanned road trips to hidden beaches, stumbling upon roadside fruit stalls, and dancing in unexpected downpours. They watched sunsets from cliffs, shared secrets under starlit skies, and spent hours in sleepy coastal towns where time felt like it had stopped. Each moment felt raw, real, and free—untethered from schedules and expectation.
        Yet amidst the laughter, Raj noticed how Maya sometimes grew quiet, her gaze drifting to the horizon as if searching for answers only she could see. On their last night by the sea, she finally shared that she might soon move abroad, chasing a dream too big to ignore. Silence hung heavy, but it was a silence of acceptance, not regret.
        When summer ended, they packed up the car, hearts heavier yet strangely grateful. Though the road ahead was uncertain, they had carved a chapter so vivid it felt destined to echo for years to come.""",
    ]

    for story in stories:
        num_sentences = 3
        highlight = generator.generate_highlight(story)
        assert type(highlight) == str
        assert len([highlight.split(".")]) <= num_sentences
