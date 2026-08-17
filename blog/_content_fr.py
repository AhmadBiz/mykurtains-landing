# -*- coding: utf-8 -*-
"""French (Québec) content for every blog post. Same slugs as English so hreflang pairs line up."""

IMG = {
    "roller": "../assets/roller.jpg",
    "curtains": "../assets/curtains.jpg",
    "roman": "../assets/roman.jpg",
    "zebra": "../assets/zebra.jpg",
    "motor": "../assets/roller-2.jpg",
    "blackout": "../assets/blockout.jpg",
    "outdoor": "https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?auto=format&fit=crop&w=1200&q=80",
    "film": "../assets/smartfilm.jpg",
    "honey": "../assets/honeycomb.jpg",
    "living": "../assets/curtains-office.jpg",
    "bedroom": "../assets/curtains-blackout-wave.jpg",
    "calm": "../assets/honeycomb-kids.jpg",
    "measure": "../assets/honeycomb-cells.jpg",
    "condo": "../assets/curtains-office.jpg",
}


def rel(href, img, tag, cat, title, blurb):
    return {"href": href, "img": img.replace("w=1200", "w=800"), "tag": tag, "cat": cat, "title": title, "blurb": blurb}


R = {
    "honey": rel("honeycomb-blinds.html", IMG["honey"], "Guide", "Alvéolaires", "Stores alvéolaires (nid d’abeille)", "Le store le plus écoénergétique."),
    "roller": rel("roller-blinds.html", IMG["roller"], "Guide", "Enrouleurs", "Stores enrouleurs : le guide complet", "Épuré, minimaliste, polyvalent."),
    "curtains": rel("curtains-and-drapes.html", IMG["curtains"], "Guide", "Rideaux", "Rideaux et draperies", "Tissus, ampleur et tombée."),
    "roman": rel("roman-shades.html", IMG["roman"], "Guide", "Bateau", "Stores bateau", "Plis soignés, luxe discret."),
    "zebra": rel("day-and-night-zebra-blinds.html", IMG["zebra"], "Guide", "Zébrés", "Stores jour et nuit (zébrés)", "Intimité et lumière en un seul store."),
    "motor": rel("motorized-blinds.html", IMG["motor"], "Guide", "Motorisés", "Stores motorisés : ça vaut le coup ?", "Ce que l’automatisation apporte vraiment."),
    "blackout": rel("blackout-blinds.html", IMG["blackout"], "Guide", "Blockout", "Store Blockout : noirceur 100 %", "Un store encadré et scellé — aucune fuite de lumière."),
    "outdoor": rel("outdoor-blinds.html", IMG["outdoor"], "Guide", "Extérieur", "Stores extérieurs", "De l’ombre pour patios et balcons."),
    "film": rel("smart-film.html", IMG["film"], "Guide", "Film intelligent", "Film intelligent", "Vitre d’intimité d’une simple pression."),
    "vs": rel("blinds-vs-curtains.html", IMG["living"], "Conseils", "Choisir", "Stores ou rideaux ?", "Lequel convient à votre pièce ?"),
    "winter": rel("best-blinds-for-montreal-winters.html", IMG["bedroom"], "Conseils", "Isolation", "Les meilleurs stores pour l’hiver montréalais", "Ce qui aide vraiment, classé."),
    "nursery": rel("blackout-blinds-for-nursery.html", IMG["calm"], "Conseils", "Sommeil", "Stores occultants pour la chambre de bébé", "Le guide des parents pour de meilleures siestes."),
    "measure": rel("how-to-measure-windows-for-blinds.html", IMG["measure"], "Conseils", "Comment faire", "Comment mesurer ses fenêtres pour des stores", "Pose intérieure ou extérieure."),
    "condo": rel("blinds-for-condos-and-apartments.html", IMG["condo"], "Conseils", "Condos", "Les meilleurs stores pour condos", "L’intimité sans perdre la vue."),
}

POSTS_FR = [
# ---------------------------------------------------------------- HONEYCOMB
dict(slug="honeycomb-blinds.html", type="guide", crumb="Stores alvéolaires", read=7, image=IMG["honey"],
 alt="Un store alvéolaire haut-bas : voile en haut qui laisse entrer la lumière, cellules occultantes en bas",
 title="Stores alvéolaires (nid d’abeille) : fonctionnement, avantages et inconvénients",
 description="Les stores alvéolaires expliqués : comment les cellules isolent vos fenêtres, simple ou double alvéole, haut-bas / bas-haut, options occultantes, avantages et inconvénients honnêtes, et s’ils conviennent à votre maison montréalaise.",
 og="Le store le plus écoénergétique qui soit — et pourquoi l’hiver montréalais en vaut la peine.",
 h1="Stores alvéolaires : le <em>surdoué</em> discret des habillages de fenêtre.",
 lede="Ils ont l’air doux et simples. En dessous, une rangée de cellules remplies d’air travaille fort : elles isolent vos fenêtres, adoucissent la lumière et étouffent le bruit de la rue. Voici comment ils fonctionnent, ce qu’ils font bien (et moins bien), et s’ils ont leur place chez vous.",
 body="""
        <h2>Qu’est-ce qu’un store alvéolaire ?</h2>
        <p>Aussi appelés <strong>stores cellulaires</strong> ou <strong>nid d’abeille</strong>, ils sont faits d’un tissu plissé collé en une rangée de cellules hexagonales — regardez-en un de côté et vous verrez la forme de nid d’abeille qui leur donne leur nom. Chaque cellule emprisonne une poche d’air immobile entre la fenêtre et la pièce.</p>
        <p>Cet air emprisonné, c’est tout l’intérêt. L’air immobile conduit mal la chaleur : un store alvéolaire agit donc comme une couche d’isolant supplémentaire sur la vitre — le même principe qu’un manteau en duvet. De tous les types de stores, les alvéolaires sont invariablement les meilleurs isolants.</p>

        <h2>Comment ça fonctionne</h2>
        <p>Le tissu est plié en accordéon et collé pour que les plis forment des cellules fermées. Levez le store et il s’empile, plat et compact, en haut ; baissez-le et les cellules s’ouvrent à pleine profondeur. Comme il n’y a ni lattes ni cordons qui traversent le tissu, la face est lisse et la lumière passe uniformément — sans rayures ni reflets.</p>
        <p>Vous choisissez l’opacité du tissu pour régler la quantité de lumière :</p>
        <ul>
          <li><strong>Voile / filtrant</strong> — une lumière du jour douce et lumineuse, avec intimité le jour.</li>
          <li><strong>Semi-opaque</strong> — plus d’ombre, lumière toujours douce.</li>
          <li><strong>Occultant</strong> — une doublure opaque dans la cellule pour une noirceur presque totale (voir plus bas).</li>
        </ul>

        <figure>
          <img src="../assets/honeycomb-cells.jpg" alt="Gros plan d’un store alvéolaire montrant les plis voile au-dessus et les cellules occultantes en dessous" />
          <figcaption>De près : plis voile en haut, cellules occultantes emprisonnant l’air en bas.</figcaption>
        </figure>
        <h3>Simple ou double alvéole</h3>
        <p>Les stores à <strong>simple alvéole</strong> ont une couche de poches ; c’est le choix courant — léger, mince et efficace. Les stores à <strong>double alvéole</strong> logent une seconde rangée de cellules dans la première, ce qui double à peu près le pouvoir isolant et bloque un peu plus de bruit. Ils sont un peu plus épais et coûtent plus cher ; on les recommande pour les pièces les plus froides : grandes fenêtres au nord, vieilles maisons montréalaises pleines de courants d’air, chambres au-dessus du garage.</p>

        <h3>Haut-bas / bas-haut</h3>
        <p>C’est la fonction qui fait craquer tout le monde. Le store peut être <em>abaissé par le haut</em> autant que relevé par le bas — vous laissez entrer la lumière et le ciel par la partie supérieure de la fenêtre tout en gardant le bas couvert pour l’intimité. Idéal pour les pièces qui donnent sur la rue et les salles de bain. La photo en haut de cette page montre exactement ça : la lumière en haut, l’occultant en bas.</p>

        <figure>
          <img src="../assets/honeycomb.jpg" alt="Store alvéolaire partiellement abaissé par le haut, montrant la section voile en haut et la section occultante en bas" />
          <figcaption>Une de nos vraies installations : store alvéolaire haut-bas, voile au-dessus, cellules occultantes en dessous.</figcaption>
        </figure>

        <h2>Avantages et inconvénients, honnêtement</h2>""",
 pros=["<strong>La meilleure isolation de tous les stores</strong> — nettement plus chaud l’hiver, plus frais l’été, factures plus basses.", "<strong>Lumière douce et uniforme</strong>, sans lignes de lattes ni reflets.", "<strong>Haut-bas / bas-haut</strong> : l’intimité sans perdre la lumière.", "<strong>Pièce plus silencieuse</strong> — les cellules absorbent une partie du bruit extérieur.", "<strong>S’empile très petit</strong> une fois relevé — vous gardez toute la vue.", "<strong>Options sans cordon et motorisées</strong> — look épuré, sécuritaire pour les enfants.", "<strong>Version occultante offerte</strong> pour chambres et chambres de bébé."],
 cons=["<strong>Moins « décoratif »</strong> que des rideaux ou des stores bateau — un look propre et minimaliste plutôt qu’une déclaration.", "<strong>Le nettoyage demande du soin</strong> — dépoussiérer avec une brosse douce ou l’aspirateur à faible puissance ; pas lavable à la machine.", "<strong>Les cellules peuvent piéger poussière ou insectes</strong> dans les plis du haut avec les années.", "<strong>L’occultant a besoin de rails latéraux</strong> pour une vraie noirceur (sinon la lumière fuit sur les bords — voir notre <a href='blackout-blinds.html'>guide occultant</a>).", "<strong>Pas pour l’extérieur humide</strong> — pour les balcons, voyez les <a href='outdoor-blinds.html'>stores extérieurs</a>."],
 glance=[("Isolation", (5, "La meilleure de sa catégorie")), ("Contrôle de la lumière", (4, "Du voile à l’occultant total")), ("Intimité", (5, "Excellente, surtout haut-bas")), ("Style", (3, "Propre et minimaliste")), ("Entretien", (3, "Dépoussiérer délicatement")), ("Pièces idéales", "Chambres, salons, bureaux à domicile, chambres de bébé, fenêtres au nord et grandes fenêtres"), ("Options", "Simple ou double alvéole · voile / semi / occultant · haut-bas/bas-haut · sans cordon · motorisé")],
 body2="""
        <h2>Pour qui c’est parfait</h2>
        <p><strong>Si votre fenêtre est froide à côtoyer en janvier, c’est votre store.</strong> Les stores alvéolaires sont la réponse pour qui veut un vrai confort et des factures de chauffage plus basses sans emballer ses fenêtres de rideaux lourds. Ils conviennent aux intérieurs modernes et minimalistes et — avec le haut-bas/bas-haut — à toute pièce qui donne sur la rue ou sur un voisin.</p>
        <p>C’est aussi notre premier choix pour les <strong>chambres et chambres de bébé</strong>, où la combinaison occultant + isolation + silence est difficile à battre.</p>
        <div class="callout"><strong>Conseil montréalais</strong><p>Les fenêtres sont généralement le point faible de l’isolation d’une maison. Sur une grande fenêtre ou une fenêtre ancienne, un store alvéolaire double peut donner à une pièce un ou deux degrés de plus au même réglage de thermostat — on le remarque surtout les nuits les plus froides.</p></div>
        <h2>Quand choisir autre chose</h2>
        <ul>
          <li>Vous voulez du drame, de la douceur ou de la couleur au mur ? Voyez les <a href="curtains-and-drapes.html">rideaux et draperies</a> ou les <a href="roman-shades.html">stores bateau</a>.</li>
          <li>Vous voulez passer de l’intimité à la vue dégagée plusieurs fois par jour ? Les <a href="day-and-night-zebra-blinds.html">stores jour et nuit (zébrés)</a> le font d’un seul geste.</li>
          <li>Vous cherchez l’option propre la moins chère pour une cuisine ou une buanderie ? Un <a href="roller-blinds.html">store enrouleur</a> est difficile à battre.</li>
        </ul>""",
 faq=[("Les stores alvéolaires en valent-ils la peine à Montréal ?", "Oui. De tous les types de stores, les cellulaires réduisent le plus la perte de chaleur par la vitre l’hiver et le gain de chaleur l’été. Avec notre longue saison de chauffage, la différence de confort est notable — surtout sur les grandes fenêtres ou celles orientées au nord."),
      ("Simple ou double alvéole : lequel choisir ?", "Simple pour la plupart des pièces. Double pour les fenêtres les plus froides (grandes, au nord, vieux simple vitrage) ou si vous voulez aussi un peu plus d’insonorisation."),
      ("Peuvent-ils être complètement occultants ?", "Oui — le tissu alvéolaire occultant a une doublure intérieure opaque. Pour une noirceur <em>totale</em> (chambre de bébé, travailleurs de nuit, cinéma maison), ajoutez des rails latéraux pour que la lumière ne fuie pas sur les bords."),
      ("Sont-ils sécuritaires pour les enfants ?", "Oui — nous recommandons le fonctionnement sans cordon ou motorisé, qui élimine complètement les cordons pendants."),
      ("Comment les nettoyer ?", "Un plumeau doux ou la brosse de l’aspirateur à faible puissance. Pour les marques, un linge humide (pas mouillé) en tapotant délicatement. Évitez de tremper le tissu."),
      ("Est-ce que vous les installez ?", "Oui — l’installation professionnelle est gratuite et incluse avec chaque commande partout à Montréal. Nous mesurons sur place pour un ajustement exact.")],
 aside_h="Voyez des échantillons alvéolaires chez vous", aside_p="Consultation gratuite à domicile. Nous apportons les tissus, mesurons vos fenêtres et vous donnons une recommandation honnête.",
 cta_h="Prêt à sentir la <em>différence</em> cet hiver ?", cta_p="Réservez une consultation gratuite. Nous mesurons, apportons des échantillons simple et double alvéole, et vous donnons un prix sur place — installation incluse.",
 related=[R["winter"], R["blackout"], R["zebra"]]),

# ---------------------------------------------------------------- ROLLER
dict(slug="roller-blinds.html", type="guide", crumb="Stores enrouleurs", read=6, image=IMG["roller"],
 alt="Stores enrouleurs dans une pièce lumineuse et moderne",
 title="Stores enrouleurs : le guide complet (tissus, avantages, inconvénients, pièces idéales)",
 description="Tout sur les stores enrouleurs : fonctionnement, types de tissus (voile, facile d’entretien, jacquard, occultant), avantages et inconvénients honnêtes, et les pièces qui leur conviennent. Sur mesure et installés gratuitement à Montréal.",
 og="Épurés, minimalistes et infiniment polyvalents — les options de tissu, et là où les stores enrouleurs brillent.",
 h1="Stores enrouleurs : le classique épuré qui <em>fait tout.</em>",
 lede="Une seule pièce de tissu sur un tube. C’est justement cette simplicité qui fait des stores enrouleurs l’habillage de fenêtre le plus populaire au monde — et qui fait que le tissu que vous choisissez compte plus que tout le reste.",
 body="""
        <h2>Qu’est-ce qu’un store enrouleur ?</h2>
        <p>Un store enrouleur, c’est un panneau de tissu plat enroulé autour d’un tube d’aluminium en haut de la fenêtre. Tirez pour couvrir, enroulez et il disparaît presque dans une mince cassette. Pas de lattes, pas de plis, pas de chichi — le tissu fait tout le travail de contrôle de la lumière et de l’intimité.</p>
        <p>Comme le mécanisme est si simple, les stores enrouleurs comptent parmi les stores sur mesure les plus abordables — et comme le tissu est un panneau plat ininterrompu, c’est la meilleure toile pour les motifs, les textures et la couleur.</p>

        <h2>Comment ça fonctionne</h2>
        <p>Le tube repose dans des supports en haut du cadre. Une <strong>chaînette</strong>, un <strong>ressort</strong> (sans cordon) ou un <strong>moteur</strong> tourne le tube pour lever et baisser le tissu. Une barre lestée en bas garde le tissu plat et droit. Ajoutez une <strong>cassette</strong> (un boîtier soigné) en haut et le rouleau est complètement caché.</p>
        <p>La vraie décision, c’est le tissu — c’est lui qui détermine ce que fait votre store :</p>
        <ul>
          <li><strong>Voile</strong> — lumière du jour douce et lumineuse, intimité le jour. Magnifique dans un salon.</li>
          <li><strong>Filtrant / tamisant</strong> — le choix de tous les jours : réduit l’éblouissement, donne de l’intimité, laisse passer la lumière.</li>
          <li><strong>Facile d’entretien / résistant à l’humidité</strong> — tissus lavables pour cuisines et salles de bain.</li>
          <li><strong>Jacquard et texturé</strong> — motifs tissés et effets lin pour un rendu plus décoratif.</li>
          <li><strong>Occultant</strong> — un tissu enduit et opaque pour les chambres ; avec des rails latéraux pour la noirceur totale (voir notre <a href="blackout-blinds.html">guide occultant</a>).</li>
        </ul>

        <h3>Chaînette, sans cordon ou motorisé ?</h3>
        <p>La <strong>chaînette</strong> est le classique et le plus économique. Le <strong>ressort sans cordon</strong> donne un look épuré et c’est le choix sécuritaire pour les chambres de bébé. Le <strong>motorisé</strong> permet des horaires et une commande par télécommande, appli ou voix — voyez <a href="motorized-blinds.html">les stores motorisés valent-ils la peine ?</a></p>

        <h2>Avantages et inconvénients, honnêtement</h2>""",
 pros=["<strong>Le store sur mesure le plus abordable</strong> — un excellent rapport qualité-prix par fenêtre.", "<strong>Le look le plus épuré et minimaliste</strong> ; disparaît presque une fois relevé.", "<strong>Énorme choix de tissus</strong> — du voile à l’occultant, uni ou à motifs.", "<strong>Facile à garder propre</strong> — une surface plate, et des tissus lavables existent.", "<strong>Idéal pour les fenêtres larges</strong> et les portes coulissantes.", "<strong>Options sans cordon et motorisées.</strong>"],
 cons=["<strong>Le moins isolant</strong> des types de stores — pour la chaleur, voyez l’<a href='honeycomb-blinds.html'>alvéolaire</a>.", "<strong>Lumière tout ou rien</strong> — pas d’inclinaison comme un store à lattes, pas de mélange voile/opaque comme le <a href='day-and-night-zebra-blinds.html'>zébré</a>.", "<strong>Fuites de lumière sur les côtés</strong> à moins d’ajouter des rails ou une pose extérieure.", "<strong>Sobre par nature</strong> — pour de la douceur et de la tombée, voyez les <a href='curtains-and-drapes.html'>rideaux</a> ou les <a href='roman-shades.html'>stores bateau</a>."],
 glance=[("Isolation", (2, "Modeste")), ("Contrôle de la lumière", (4, "Du voile à l’occultant selon le tissu")), ("Intimité", (4, "Selon le tissu")), ("Style", (3, "Propre, polyvalent")), ("Entretien", (5, "Très facile")), ("Rapport qualité-prix", (5, "Le meilleur par fenêtre")), ("Pièces idéales", "Cuisines, salles de bain, bureaux, salons, fenêtres larges"), ("Options", "Chaînette · sans cordon · motorisé · cassette · rails latéraux · double (zébré)")],
 body2="""
        <h2>Pour qui c’est parfait</h2>
        <p><strong>Si vous voulez un look propre et moderne à un budget raisonnable, commencez ici.</strong> Les stores enrouleurs sont notre recommandation pour les cuisines et salles de bain (tissus faciles d’entretien), les bureaux à domicile (contrôle de l’éblouissement), et partout où vous voulez une fenêtre dégagée. C’est aussi le choix évident pour les très grandes fenêtres et les portes-patio, là où les autres styles deviennent lourds.</p>
        <div class="callout"><strong>Astuce de pro</strong><p>Choisissez le tissu selon la <em>fonction</em>, pas seulement la couleur : tamisant pour les aires de vie, occultant pour les chambres, résistant à l’humidité près de l’eau. Nous apportons le nuancier complet à la consultation pour que vous les voyiez contre votre mur, dans votre lumière.</p></div>
        <h2>Quand choisir autre chose</h2>
        <ul>
          <li>Fenêtre froide ? Un <a href="honeycomb-blinds.html">store alvéolaire</a> isole beaucoup mieux.</li>
          <li>Vous voulez alterner vue et intimité toute la journée ? Les <a href="day-and-night-zebra-blinds.html">stores zébrés</a> le font d’un geste.</li>
          <li>Vous voulez de la chaleur et de la douceur au mur ? <a href="curtains-and-drapes.html">Rideaux</a> ou <a href="roman-shades.html">stores bateau</a>.</li>
        </ul>""",
 faq=[("Les stores enrouleurs conviennent-ils aux chambres ?", "Oui, avec un tissu occultant — et ajoutez des rails latéraux si vous voulez la noirceur totale. Pour le meilleur environnement de sommeil, un alvéolaire occultant ajoute aussi isolation et silence."),
      ("Peut-on nettoyer les stores enrouleurs ?", "Facilement. Dépoussiérez ou passez l’aspirateur à faible puissance ; essuyez les tissus faciles d’entretien avec un linge humide. C’est le type de store qui demande le moins d’entretien."),
      ("Les stores enrouleurs bloquent-ils la chaleur ?", "Les tissus réfléchissants et occultants réduisent nettement le gain de chaleur l’été. Pour l’isolation hivernale, les stores alvéolaires (cellulaires) sont le meilleur choix."),
      ("Sont-ils sécuritaires pour les enfants ?", "Oui — choisissez le fonctionnement sans cordon (ressort) ou motorisé, qui élimine les chaînettes pendantes."),
      ("Est-ce que vous les installez ?", "Oui — l’installation est gratuite et incluse avec chaque commande partout à Montréal. Nous mesurons sur place pour un ajustement exact.")],
 aside_h="Voyez les tissus enrouleurs chez vous", aside_p="Consultation gratuite à domicile. Nous apportons le nuancier, mesurons vos fenêtres et recommandons le bon tissu pour chaque pièce.",
 cta_h="Look épuré, prix honnête — <em>installé gratuitement.</em>", cta_p="Réservez une consultation gratuite. Nous mesurons, apportons des échantillons de tissu et vous donnons un prix sur place.",
 related=[R["zebra"], R["blackout"], R["honey"]]),

# ---------------------------------------------------------------- CURTAINS
dict(slug="curtains-and-drapes.html", type="guide", crumb="Rideaux et draperies", read=7, image=IMG["curtains"],
 alt="Rideaux jusqu’au sol encadrant une fenêtre de chambre lumineuse",
 title="Rideaux et draperies : tissus, ampleur et la bonne tombée",
 description="Guide complet des rideaux et draperies sur mesure : voile ou occultant, doublure, ampleur, styles de plis, rail ou tringle, et comment mesurer la tombée. Sur mesure et installés gratuitement à Montréal.",
 og="Pourquoi les rideaux gagnent encore en douceur et en drame — et les détails de mesure qui font tout.",
 h1="Rideaux et draperies : douceur, drame, et <em>la bonne tombée.</em>",
 lede="Rien ne change autant l’atmosphère d’une pièce qu’un tissu qui tombe du plafond au plancher. Les rideaux ajoutent chaleur, hauteur et une finition qu’aucun store rigide ne peut égaler — s’ils sont faits et posés correctement. Voici ce qui compte vraiment.",
 body="""
        <h2>Rideaux ou draperies : y a-t-il une différence ?</h2>
        <p>En gros : les <strong>rideaux</strong> sont plus légers, souvent sans doublure ; les <strong>draperies</strong> sont plus lourdes, doublées, plus habillées. En pratique, nous faisons les deux sur mesure et le choix tient surtout au <em>poids du tissu, à la doublure et à la fonction</em>. Beaucoup de pièces combinent un voile pour le jour et une draperie doublée par-dessus pour le soir — le look superposé qu’on voit dans les maisons bien conçues.</p>

        <h2>Les décisions qui comptent</h2>
        <h3>1. Tissu et opacité</h3>
        <ul>
          <li><strong>Voile</strong> — lumière douce, intimité le jour, effet aérien.</li>
          <li><strong>Lin et effet lin</strong> — décontracté, texturé, très actuel.</li>
          <li><strong>Velours et tissages lourds</strong> — luxe, chaleur, absorption du son.</li>
          <li><strong>Doublure occultante</strong> — chambres et salles de cinéma.</li>
        </ul>
        <h3>2. La doublure</h3>
        <p>La doublure, c’est ce qui sépare un rideau qui a l’air bien d’un rideau qui a l’air <em>cher</em>. Elle donne du corps pour que le tissu tombe en plis nets, protège le tissu de face de la décoloration au soleil et — avec une doublure thermique ou occultante — ajoute isolation et noirceur.</p>
        <figure>
          <img src="../assets/curtains-blackout-wave.jpg" alt="Gros plan de draperies occultantes à plis vague à côté d’une fenêtre montréalaise enneigée" />
          <figcaption>Draperies occultantes à vague, en plein hiver montréalais. Le corps du tissu vient de la doublure.</figcaption>
        </figure>
        <h3>3. L’ampleur</h3>
        <p>L’ampleur, c’est la quantité de tissu par rapport à la largeur de la fenêtre. Les rideaux trop justes sont l’erreur la plus fréquente. Nous utilisons environ <strong>2 à 2,5 fois la largeur du rail</strong> pour que les rideaux paraissent généreux, ouverts comme fermés.</p>
        <h3>4. Le style de tête (plis)</h3>
        <p><strong>Vague / pli S</strong> — ondulations douces et régulières ; le favori moderne sur rail. <strong>Pli pincé</strong> — ajusté, classique. <strong>Œillets</strong> — décontracté, sur tringle. <strong>Pli crayon</strong> — traditionnel et économique.</p>
        <figure>
          <img src="../assets/curtains-sheer-tall.jpg" alt="Rideaux voile à vague double hauteur sur rail au plafond devant une vue de lac" />
          <figcaption>Voiles à vague sur rail au plafond, du plancher au (très haut) plafond — une de nos installations.</figcaption>
        </figure>
        <h3>5. Rail ou tringle, et hauteur de pose</h3>
        <p>Un <strong>rail fixé au plafond</strong> donne le look le plus propre et le plus haut, et glisse en silence — notre recommandation habituelle. Posez haut et large : accrocher les rideaux juste au-dessus du cadre et les prolonger de chaque côté agrandit visuellement la fenêtre et la pièce.</p>
        <h3>6. La tombée (longueur)</h3>
        <p><strong>Effleurer le plancher</strong> (environ 1 cm au-dessus) pour une finition nette et ajustée. <strong>Casser</strong> (2 à 3 cm sur le plancher) pour un look détendu et luxueux. <strong>Traîner</strong> pour le drame complet. Jamais à mi-mur. C’est pour obtenir cette précision que nous mesurons chaque fenêtre nous-mêmes.</p>

        <h2>Avantages et inconvénients, honnêtement</h2>""",
 pros=["<strong>Douceur, chaleur et drame inégalés</strong> — transforme l’atmosphère d’une pièce.", "<strong>Fait paraître les plafonds plus hauts</strong> et les fenêtres plus grandes quand on pose haut et large.", "<strong>Excellente isolation et absorption du son</strong> avec doublure.", "<strong>Choix infini</strong> de tissus, couleurs et motifs.", "<strong>Se superpose à merveille</strong> avec des voiles ou des stores.", "<strong>Rails motorisés</strong> offerts."],
 cons=["<strong>Prend de la place au mur</strong> une fois ouvert (l’empilement) — à prévoir.", "<strong>Pas idéal près de l’eau ou de la cuisson</strong> — les cuisines et salles de bain conviennent mieux aux stores.", "<strong>Prend la poussière et demande un nettoyage périodique</strong> ; vérifiez l’entretien du tissu.", "<strong>Coûte plus qu’un store enrouleur de base</strong> à cause de la quantité de tissu et de la doublure.", "<strong>Les détails ne pardonnent pas</strong> — les mauvaises mesures se voient. (Nous mesurons pour vous.)"],
 glance=[("Isolation", (4, "Très bonne avec doublure")), ("Contrôle de la lumière", (4, "Du voile à l’occultant total")), ("Intimité", (4, "Excellente une fois fermés")), ("Style", (5, "L’option affirmée")), ("Entretien", (3, "Nettoyage périodique")), ("Pièces idéales", "Salons, chambres, salles à manger, fenêtres hautes"), ("Options", "Voile / lin / velours / occultant · doublé · vague / pincé / œillets · rail ou tringle · motorisé")],
 body2="""
        <h2>Pour qui c’est parfait</h2>
        <p><strong>Si vous voulez que la pièce paraisse chaleureuse, finie et un brin luxueuse, la réponse, ce sont les rideaux.</strong> C’est notre première recommandation pour les salons et les chambres, pour les fenêtres hautes ou vedettes, et pour quiconque trouve les stores rigides un peu cliniques. Superposez un voile sous une draperie doublée et vous obtenez une lumière douce le jour et une intimité douillette le soir.</p>
        <div class="callout"><strong>Le look superposé</strong><p>Notre combinaison la plus demandée — et exactement ce que montre la photo en haut de cette page : un <em>rideau voile à vague</em> sur rail au plafond pour la lumière du jour, avec une <em>draperie occultante doublée</em> devant pour le soir. Ou un <a href="honeycomb-blinds.html">store alvéolaire</a> derrière pour l’isolation. Le meilleur des deux, et ça photographie superbement.</p></div>
        <h2>Quand choisir autre chose</h2>
        <ul>
          <li>Cuisine, salle de bain ou fenêtre juste à côté de l’évier ? Un <a href="roller-blinds.html">store enrouleur</a> lavable.</li>
          <li>Peu d’espace au mur, ou envie d’un pli ajusté plutôt qu’une tombée ? <a href="roman-shades.html">Stores bateau</a>.</li>
          <li>Besoin d’isolation sans le volume de tissu ? <a href="honeycomb-blinds.html">Stores alvéolaires</a>.</li>
        </ul>""",
 faq=[("À quelle hauteur poser les rideaux ?", "Le plus haut possible — idéalement au plafond ou juste en dessous, et en dépassant de 15 à 25 cm de chaque côté de la fenêtre. Ça agrandit visuellement la fenêtre et la pièce."),
      ("Les rideaux doivent-ils toucher le plancher ?", "Oui, ou presque. « Effleurez » le plancher (environ 1 cm au-dessus) pour un look ajusté, ou « cassez » de 2 à 3 cm dessus pour un rendu détendu et luxueux. Des rideaux qui s’arrêtent à mi-mur ont l’air inachevés."),
      ("Qu’est-ce que l’ampleur ?", "Le rapport entre la largeur du tissu et celle du rail. Nous utilisons environ 2 à 2,5 fois pour que les rideaux paraissent généreux. Les rideaux trop justes sont l’erreur numéro un."),
      ("Les rideaux isolent-ils bien ?", "Les rideaux doublés — surtout avec doublure thermique ou occultante — isolent très bien et absorbent aussi le son. Pour la meilleure isolation, combinez-les avec un store alvéolaire."),
      ("Est-ce que vous les fabriquez et les installez ?", "Oui — chaque rideau est fait sur mesure pour votre fenêtre et installé gratuitement partout à Montréal, rails compris.")],
 aside_h="Voyez les tissus dans votre lumière", aside_p="Consultation gratuite à domicile. Nous apportons des échantillons et mesurons pour que la tombée et l’ampleur soient exactement justes.",
 cta_h="Un tissu qui tombe <em>exactement</em> bien.", cta_p="Réservez une consultation gratuite. Nous mesurons chaque fenêtre, apportons échantillons de tissu et de doublure, et installons gratuitement.",
 related=[R["roman"], R["vs"], R["honey"]]),

# ---------------------------------------------------------------- ROMAN
dict(slug="roman-shades.html", type="guide", crumb="Stores bateau", read=6, image=IMG["roman"],
 alt="Élégants stores bateau encadrant une fenêtre",
 title="Stores bateau : plis soignés, luxe discret (fonctionnement, avantages, inconvénients)",
 description="Les stores bateau expliqués : comment ils se plient et s’empilent, styles plat ou bouillonné, options de doublure et occultantes, avantages et inconvénients honnêtes, et les pièces qui leur conviennent. Sur mesure et installés gratuitement à Montréal.",
 og="Le look doux et structuré — comment ils s’empilent, quels tissus fonctionnent, et les pièces faites pour eux.",
 h1="Stores bateau : le pli soigné qui respire le <em>luxe discret.</em>",
 lede="Un store bateau, c’est du tissu qui se replie en plis horizontaux nets au lieu de s’enrouler. Vous obtenez la douceur d’un rideau avec l’encombrement réduit d’un store — c’est pourquoi les designers y reviennent sans cesse.",
 body="""
        <h2>Qu’est-ce qu’un store bateau ?</h2>
        <p>Un store bateau, c’est un panneau de tissu plat avec des baguettes ou des coutures horizontales cousues au dos. Quand vous le relevez, le tissu se rassemble en une pile de plis réguliers en haut de la fenêtre ; baissez-le et il pend, plat et lisse. C’est un store fait de tissu de draperie — structuré mais doux.</p>

        <h2>Comment ça fonctionne</h2>
        <p>Des cordons (ou un moteur) montent au dos du store à travers des anneaux sur chaque baguette. Tirez, et le bas monte pli par pli. Comme il est fait de vrai tissu de draperie, un store bateau peut être <strong>doublé</strong> pour le corps, <strong>doublé thermique</strong> pour l’isolation, ou <strong>doublé occultant</strong> pour les chambres.</p>
        <h3>Les styles</h3>
        <ul>
          <li><strong>Bateau plat</strong> — face lisse et propre une fois baissé ; plis nets une fois relevé. Le favori moderne ; parfait pour les motifs.</li>
          <li><strong>Bouillonné (à boucles)</strong> — plis doux permanents même complètement baissé. Plus chaleureux, plus traditionnel.</li>
          <li><strong>Décontracté</strong> — une courbe douce à l’ourlet du bas pour un look plus souple (idéal sur les fenêtres qu’on relève rarement).</li>
        </ul>
        <h3>Le tissu</h3>
        <p>Le lin et les tissages effet lin sont le choix classique — de la texture sans lourdeur. Le coton et ses mélanges prennent bien les motifs. Les tissages plus lourds paraissent plus riches. Presque tout tissu de draperie fonctionne, et c’est là que les stores bateau battent tous les autres stores pour le choix.</p>

        <h2>Avantages et inconvénients, honnêtement</h2>""",
 pros=["<strong>La douceur et l’élégance</strong> du tissu, dans l’encombrement d’un store.", "<strong>Énorme choix de tissus</strong> — texture, couleur, motifs.", "<strong>Peut être doublé</strong> — thermique ou occultant — pour l’isolation et la noirceur.", "<strong>Excellent dans les cuisines et les petites fenêtres</strong> où des rideaux seraient de trop.", "<strong>Se superpose à merveille</strong> avec des voiles ou des rideaux.", "<strong>Options sans cordon et motorisées.</strong>"],
 cons=["<strong>Les plis s’empilent en haut</strong> et couvrent une partie de la fenêtre une fois relevé (sauf posé au-dessus du cadre).", "<strong>Coûte plus qu’un store enrouleur</strong> — vrai tissu plus doublure et confection.", "<strong>Pas pour les très grandes largeurs</strong> — au-delà d’environ 2 m ils deviennent lourds ; pensez à deux stores ou à des rideaux.", "<strong>Pas idéal dans une salle de bain embuée</strong> sauf si le tissu est choisi avec soin.", "<strong>Le nettoyage, c’est dépoussiérer / aspirer</strong> — pas un coup de linge."],
 glance=[("Isolation", (4, "Très bonne avec doublure")), ("Contrôle de la lumière", (4, "Du filtrant à l’occultant selon la doublure")), ("Intimité", (4, "Excellente une fois baissé")), ("Style", (5, "Le favori des designers")), ("Entretien", (3, "Dépoussiérer / aspirer")), ("Pièces idéales", "Salons, salles à manger, chambres, cuisines (avec soin), petites fenêtres et fenêtres vedettes"), ("Options", "Plat / bouillonné / décontracté · doublé / thermique / occultant · sans cordon · motorisé")],
 body2="""
        <h2>Pour qui c’est parfait</h2>
        <p><strong>Si vous aimez la douceur du tissu mais que vous le voulez bien rangé, c’est votre store.</strong> Les stores bateau sont notre choix pour les salles à manger, les salons et les chambres où des rideaux feraient trop de tissu, pour les cuisines (un bateau plat en tissu lavable au-dessus de l’évier, c’est un classique), et pour quiconque a un goût « discrètement cher ».</p>
        <div class="callout"><strong>Conseil de pose</strong><p>Posez le store <em>au-dessus</em> du cadre de la fenêtre (pose extérieure) pour que la pile relevée repose sur le mur, pas sur la vitre. Vous gardez toute la vue et la fenêtre paraît plus haute. On vous conseille sur place.</p></div>
        <h2>Quand choisir autre chose</h2>
        <ul>
          <li>Très grande fenêtre ou porte-patio ? <a href="curtains-and-drapes.html">Rideaux</a> ou <a href="roller-blinds.html">store enrouleur</a>.</li>
          <li>Priorité à l’isolation ? Un <a href="honeycomb-blinds.html">store alvéolaire</a>.</li>
          <li>Vous voulez alterner vue et intimité sans cesse ? <a href="day-and-night-zebra-blinds.html">Stores zébrés</a>.</li>
        </ul>""",
 faq=[("Les stores bateau conviennent-ils aux chambres ?", "Oui — avec une doublure occultante ils sont excellents, et plus doux qu’un store rigide. Ajoutez des rails latéraux ou une pose extérieure pour réduire la lumière sur les bords."),
      ("Bateau plat ou bouillonné ?", "Plat pour un look propre et moderne (et pour les tissus à motifs). Bouillonné pour un rendu plus doux et traditionnel, avec des plis permanents."),
      ("Peut-on motoriser un store bateau ?", "Oui. Les stores bateau motorisés sont silencieux et très pratiques sur les fenêtres difficiles d’accès ou nombreuses."),
      ("Sont-ils difficiles à nettoyer ?", "Dépoussiérez ou passez l’aspirateur à faible puissance. Certains tissus se nettoient localement. Ce n’est pas une surface lavable comme un enrouleur, alors pour les cuisines nous orientons vers des tissus lavables."),
      ("Est-ce que vous les installez ?", "Oui — sur mesure et installés gratuitement partout à Montréal.")],
 aside_h="Touchez les tissus chez vous", aside_p="Consultation gratuite à domicile. Nous apportons des échantillons de lin et de coton et mesurons pour que les plis tombent exactement bien.",
 cta_h="Des plis soignés, <em>sur mesure.</em>", cta_p="Réservez une consultation gratuite. Nous mesurons, apportons des échantillons de tissu et installons gratuitement.",
 related=[R["curtains"], R["honey"], R["blackout"]]),

# ---------------------------------------------------------------- ZEBRA
dict(slug="day-and-night-zebra-blinds.html", type="guide", crumb="Jour et nuit (zébrés)", read=6, image=IMG["zebra"],
 alt="Stores zébrés jour et nuit aux bandes voile et opaques alternées",
 title="Stores jour et nuit (zébrés) expliqués : fonctionnement, avantages, inconvénients",
 description="Les stores zébrés (jour et nuit) expliqués : comment fonctionnent les bandes voile et opaques alternées, versions occultantes, avantages et inconvénients honnêtes, et les pièces qui leur conviennent. Sur mesure et installés gratuitement à Montréal.",
 og="Des bandes voile et opaques qui glissent l’une sur l’autre — intimité et lumière du jour en un seul store.",
 h1="Stores jour et nuit : intimité et lumière du jour en <em>un seul</em> store.",
 lede="Aussi appelés stores zébrés ou doubles. Deux couches de tissu rayées de bandes voile et opaques alternées glissent l’une sur l’autre — alignez les voiles pour une vue tamisée, alignez les opaques pour l’intimité, et tout ce qu’il y a entre les deux. C’est le store qui change d’avis avec vous.",
 body="""
        <h2>Qu’est-ce qu’un store jour et nuit ?</h2>
        <p>Imaginez un store enrouleur dont le tissu est une boucle continue, rayée de bandes <strong>voile</strong> et <strong>opaques</strong> alternées. La boucle descend devant et remonte derrière, de sorte que les deux couches se chevauchent. Bougez légèrement le store et les bandes se décalent l’une par rapport à l’autre :</p>
        <ul>
          <li><strong>Voile sur voile</strong> — une vue ouverte et tamisée ; la lumière du jour entre à flots.</li>
          <li><strong>Opaque sur voile</strong> — intimité totale, lumière douce à travers la couche voile.</li>
          <li><strong>N’importe où entre les deux</strong> — réglez exactement la lumière que vous voulez.</li>
        </ul>
        <p>Vous pouvez toujours l’enrouler complètement comme un enrouleur normal quand vous voulez la fenêtre dégagée.</p>

        <h2>Comment ça fonctionne</h2>
        <p>Une chaînette, un ressort ou un moteur fait tourner la boucle de tissu autour d’un tube. Comme le mécanisme est un enrouleur, les stores jour et nuit ont la même cassette mince, le même look propre et un prix semblable à un bon enrouleur — avec beaucoup plus de contrôle. Ils existent en versions <strong>filtrantes</strong> et à <strong>bandes occultantes</strong> (les bandes opaques sont occultantes, donc bandes alignées, la pièce devient très sombre — pas tout à fait noire, parce que les bandes voile restent).</p>

        <h2>Avantages et inconvénients, honnêtement</h2>""",
 pros=["<strong>Intimité et vue avec un seul store</strong> — pas besoin d’un voile plus un store.", "<strong>Lumière infiniment réglable</strong> d’un petit mouvement.", "<strong>Look moderne et rayé</strong> qui convient aux pièces contemporaines.", "<strong>Simplicité de l’enrouleur</strong> et cassette mince.", "<strong>Excellent rapport qualité-prix</strong> pour la flexibilité obtenue.", "<strong>Options sans cordon et motorisées.</strong>"],
 cons=["<strong>Pas vraiment occultant</strong> — les bandes voile laissent toujours passer un peu de lumière. Pour la noirceur totale, voyez le <a href='blackout-blinds.html'>store Blockout</a>.", "<strong>Isolation modeste</strong> — comme un enrouleur. Fenêtre froide ? <a href='honeycomb-blinds.html'>Alvéolaire</a>.", "<strong>Les rayures sont un look</strong> — on aime ou on n’aime pas.", "<strong>Deux couches de tissu</strong>, donc un rouleau un peu plus gros sur les très hautes fenêtres."],
 glance=[("Isolation", (2, "Modeste")), ("Contrôle de la lumière", (5, "Infiniment réglable")), ("Intimité", (4, "Excellente (bandes alignées)")), ("Style", (4, "Moderne, rayé")), ("Entretien", (4, "Facile")), ("Rapport qualité-prix", (5, "Excellent")), ("Pièces idéales", "Salons, bureaux à domicile, cuisines, pièces sur la rue"), ("Options", "Bandes filtrantes ou occultantes · chaînette / sans cordon / motorisé · cassette")],
 body2="""
        <h2>Pour qui c’est parfait</h2>
        <p><strong>Si votre fenêtre donne sur la rue ou sur un voisin et que vous rêvez d’avoir la vue <em>et</em> l’intimité, c’est le store.</strong> Les stores jour et nuit sont notre première recommandation pour les salons et les bureaux à domicile, et pour quiconque touche à ses stores dix fois par jour et veut que ce soit sans effort.</p>
        <div class="callout"><strong>Le favori montréalais</strong><p>Les stores zébrés comptent parmi nos produits les plus installés dans les condos et duplex de la ville — grandes fenêtres, voisins proches, et beaucoup de lumière à gérer. Ils règlent les trois.</p></div>
        <h2>Quand choisir autre chose</h2>
        <ul>
          <li>Besoin de noirceur totale (chambre, chambre de bébé) ? Un <a href="blackout-blinds.html">store Blockout</a>.</li>
          <li>Fenêtre froide ou au nord ? <a href="honeycomb-blinds.html">Stores alvéolaires</a>.</li>
          <li>Vous préférez une face unie, sans rayures ? Un <a href="roller-blinds.html">store enrouleur</a> avec un rideau voile.</li>
        </ul>""",
 faq=[("Les stores zébrés sont-ils occultants ?", "Les versions à bandes occultantes rendent une pièce très sombre, mais les bandes voile laissent toujours passer un peu de lumière — donc pas 100 %. Pour les chambres de bébé et les travailleurs de nuit, choisissez le store Blockout — un store encadré qui scelle chaque bord."),
      ("Voit-on à travers les stores zébrés la nuit ?", "Bandes opaques alignées, non — les rayures opaques se chevauchent et bloquent la vue vers l’intérieur. Voiles alignés, une silhouette peut être visible quand la pièce est éclairée, comme avec tout voile."),
      ("Conviennent-ils aux grandes fenêtres ?", "Oui — c’est un mécanisme d’enrouleur, donc ils gèrent bien les fenêtres larges et les portes-patio."),
      ("Chaînette ou motorisé ?", "Les deux fonctionnent bien. Le motorisé est particulièrement agréable ici parce que vous les ajusterez souvent ; une télécommande ou un horaire rend ça sans effort."),
      ("Est-ce que vous les installez ?", "Oui — sur mesure et installés gratuitement partout à Montréal.")],
 aside_h="Essayez les bandes chez vous", aside_p="Consultation gratuite à domicile. Nous apportons des échantillons pour que vous voyiez les bandes voile et occultantes contre votre fenêtre.",
 cta_h="La vue le jour, l’intimité la nuit — <em>un seul store.</em>", cta_p="Réservez une consultation gratuite. Nous mesurons, apportons des échantillons et installons gratuitement.",
 related=[R["roller"], R["condo"], R["blackout"]]),

# ---------------------------------------------------------------- MOTORIZED
dict(slug="motorized-blinds.html", type="guide", crumb="Stores motorisés", read=7, image=IMG["motor"],
 alt="Stores occultants motorisés dans une chambre paisible",
 title="Stores motorisés : ça vaut le coup ? (coûts, options, avantages, inconvénients)",
 description="Les stores motorisés expliqués : fonctionnement, commande par télécommande / appli / voix, horaires, batterie ou filaire, quels stores se motorisent, avantages et inconvénients honnêtes, et si ça vaut la peine. Installés gratuitement à Montréal.",
 og="Télécommandes, horaires, commande vocale — ce que la motorisation apporte vraiment, et ce que ça coûte.",
 h1="Stores motorisés : est-ce que ça vaut <em>vraiment</em> le coup ?",
 lede="Appuyez sur un bouton — ou dites un mot — et tous les stores de la pièce glissent en place. <strong>Chacun de nos produits peut être motorisé</strong> — enrouleurs, zébrés, alvéolaires, stores bateau, stores Blockout et rails de rideaux. Voici ce que ça apporte, ce que ça coûte et quand ça en vaut la peine.",
 body="""
        <h2>Qu’est-ce qu’un store motorisé ?</h2>
        <p>N’importe quel store ou rideau équipé d’un petit moteur silencieux à la place d’une chaînette ou d’un cordon. Vous le commandez avec une <strong>télécommande</strong>, un <strong>interrupteur mural</strong>, une <strong>appli</strong> ou la <strong>voix</strong> (Google, Alexa, Maison d’Apple), et vous pouvez programmer des <strong>horaires</strong> — ouvrir au lever du soleil, fermer au crépuscule, tout automatiquement.</p>
        <p><strong>Tout ce que nous vendons peut être motorisé :</strong> les <a href="roller-blinds.html">stores enrouleurs</a>, les <a href="day-and-night-zebra-blinds.html">stores zébrés</a>, les <a href="honeycomb-blinds.html">stores alvéolaires</a>, les <a href="roman-shades.html">stores bateau</a>, le <a href="blackout-blinds.html">store Blockout</a>, les <a href="outdoor-blinds.html">stores extérieurs</a> et les <a href="curtains-and-drapes.html">rails de rideaux</a>. C’est un choix par fenêtre, et vous pouvez mélanger motorisé et manuel.</p>

        <h2>Comment ça fonctionne</h2>
        <h3>L’alimentation</h3>
        <ul>
          <li><strong>Batterie rechargeable</strong> — le moteur loge dans le tube ; rechargez-le deux ou trois fois par année avec un câble USB. Pas de filage, pas d’électricien. Notre choix le plus courant.</li>
          <li><strong>Filaire</strong> — alimenté par le secteur ; idéal pour les constructions neuves ou les rénovations où le filage est facile. Ne se recharge jamais.</li>
          <li><strong>Bande solaire</strong> — un mince panneau sur la fenêtre garde les batteries chargées.</li>
        </ul>
        <h3>La commande</h3>
        <p>Une télécommande (mono ou multicanal) est le plus simple. Ajoutez un <strong>concentrateur</strong> et vous obtenez la commande par appli, les horaires et la voix. Groupez les stores par pièce, créez des scènes « Bonjour » et « Cinéma », et contrôlez toute la maison depuis votre téléphone — même à distance.</p>

        <h2>Là où la motorisation est vraiment géniale</h2>
        <ul>
          <li><strong>Fenêtres difficiles d’accès</strong> — hautes, derrière un meuble, au-dessus d’un évier ou d’un bain.</li>
          <li><strong>Plusieurs fenêtres à la fois</strong> — un bouton, tout le salon.</li>
          <li><strong>Sommeil et routine</strong> — l’occultant de la chambre s’ouvre doucement à votre heure de réveil.</li>
          <li><strong>Énergie et soleil</strong> — programmez les stores pour bloquer le soleil de l’après-midi l’été et laisser entrer la lumière l’hiver.</li>
          <li><strong>Sécurité</strong> — des stores qui bougent selon un horaire pendant votre absence donnent l’impression d’une maison habitée.</li>
          <li><strong>Sécurité des enfants et des animaux</strong> — aucun cordon.</li>
        </ul>

        <h2>Avantages et inconvénients, honnêtement</h2>""",
 pros=["<strong>Sans effort</strong> — surtout avec des fenêtres nombreuses, hautes ou difficiles.", "<strong>Horaires et scènes</strong> qui se font tout seuls.", "<strong>Sans cordon = le plus sécuritaire</strong> pour les enfants et les animaux, et le look le plus épuré.", "<strong>Compatible maison intelligente</strong> — Google, Alexa, Apple.", "<strong>Ajoute une vraie valeur</strong> à une maison.", "<strong>Les versions à batterie n’exigent aucun filage.</strong>"],
 cons=["<strong>Coûte plus par store</strong> que le manuel — le moteur et la commande s’ajoutent au prix.", "<strong>Les batteries doivent être rechargées</strong> quelques fois par année (ou passez au filaire / solaire).", "<strong>Un appareil de plus</strong> — un concentrateur pour l’appli/la voix, des télécommandes à ne pas perdre.", "<strong>Les moteurs peuvent éventuellement devoir être remplacés</strong> (ils durent des années, et se remplacent).", "<strong>Excessif pour une seule petite fenêtre facile</strong> que vous touchez rarement."],
 glance=[("Commodité", (5, "Tout l’intérêt")), ("Sécurité", (5, "Aucun cordon")), ("Maison intelligente", (5, "Appli, voix, horaires")), ("Coût", (2, "Plus élevé que le manuel")), ("Entretien", (4, "Recharge occasionnelle")), ("Idéal pour", "Fenêtres multiples / hautes / difficiles d’accès, chambres, salons, bureaux à domicile"), ("Options", "Batterie · filaire · solaire · télécommande · interrupteur mural · appli · voix · horaires")],
 body2="""
        <h2>Alors — ça vaut le coup ?</h2>
        <p><strong>Oui, quand vous avez plus de deux fenêtres dans une pièce, une fenêtre difficile d’accès, ou une chambre où vous aimeriez vous réveiller à la lumière du jour.</strong> C’est la plupart des salons et des chambres montréalais. Là où ça <em>ne</em> vaut <em>pas</em> le coup : une seule petite fenêtre que vous touchez rarement. Notre conseil honnête est habituellement de motoriser les pièces où vous vivez le plus et de garder des stores manuels ailleurs — vous obtenez la commodité là où ça compte et gardez le budget raisonnable.</p>
        <div class="callout"><strong>Bon à savoir</strong><p>La motorisation se décide par store, et vous pouvez mélanger — motorisé au salon et dans la chambre, manuel dans la buanderie. On passe ça en revue pièce par pièce à votre consultation.</p></div>""",
 faq=[("Combien coûtent les stores motorisés ?", "Le moteur et les commandes s’ajoutent au prix du store — le montant dépend du type de store, de sa taille et de si vous voulez seulement une télécommande ou la commande complète par appli/voix. Nous donnons un prix par fenêtre à votre consultation gratuite, sans engagement."),
      ("Les stores motorisés ont-ils besoin d’un électricien ?", "Pas les stores à batterie — le choix le plus courant — que nous installons comme n’importe quel store et que vous rechargez par USB quelques fois par année. Les options filaires ont besoin du secteur et conviennent aux rénovations et constructions neuves."),
      ("Combien de temps durent les batteries ?", "Généralement plusieurs mois entre les recharges avec un usage quotidien normal. Les bandes solaires peuvent les garder chargées indéfiniment."),
      ("Fonctionnent-ils avec Google Home / Alexa / Maison d’Apple ?", "Oui, avec un concentrateur. Vous pouvez ensuite utiliser la voix, l’appli, les horaires et les scènes."),
      ("Quels stores peuvent être motorisés ?", "Enrouleurs, zébrés, alvéolaires, stores bateau et rails de rideaux — presque tout ce que nous fabriquons."),
      ("Est-ce que vous les installez ?", "Oui — l’installation et la configuration sont gratuites et incluses partout à Montréal.")],
 aside_h="Voyez un moteur à l’œuvre", aside_p="Consultation gratuite à domicile. Nous ferons la démonstration de la télécommande et de l’appli, et vous conseillerons sur les pièces qui valent la motorisation.",
 cta_h="Tous les stores, <em>un seul bouton.</em>", cta_p="Réservez une consultation gratuite. Nous mesurons, faisons la démonstration des commandes et installons gratuitement — pas d’électricien requis pour les modèles à batterie.",
 related=[R["blackout"], R["honey"], R["zebra"]]),

# ---------------------------------------------------------------- BLOCKOUT
dict(slug="blackout-blinds.html", type="guide", crumb="Store Blockout", read=6, image=IMG["blackout"],
 alt="Un store Blockout noir encadré et scellé dans une fenêtre de chambre, bloquant toute la lumière",
 title="Store Blockout : le store encadré qui bloque 100 % de la lumière",
 description="Le store Blockout est un store encadré et scellé sur les bords qui donne une vraie noirceur à 100 % — sans halo, sans fuites latérales. Comment fonctionne le cadre, pour qui c’est fait, options sans cordon et motorisées, avantages et inconvénients honnêtes. Installé gratuitement à Montréal.",
 og="Un store encadré et scellé qui bloque 100 % de la lumière — sans halo, sans fuites. Une vraie noirceur pour un vrai sommeil.",
 h1="Store Blockout : le store qui rend enfin une pièce <em>complètement</em> noire.",
 lede="Tous les stores « occultants » que vous avez eus laissaient passer la lumière sur les bords. Le store Blockout, non — et la raison est simple : ce n’est pas juste un tissu, c’est un tissu dans un cadre qui scelle chaque bord de la fenêtre. Voici comment ça fonctionne et pour qui c’est fait.",
 body="""
        <h2>Le problème des stores occultants ordinaires</h2>
        <p>Le tissu occultant est entièrement opaque, mais un store ordinaire pend à quelques millimètres du cadre. La lumière s’engouffre autour de ces bords en barres lumineuses — et un matin d’été à Montréal, ce halo arrive avant 5 h. On peut ajouter des rails, des rideaux et du chevauchement pour le combattre, mais on colmate des fentes que le store lui-même crée.</p>
        <figure>
          <img src="../assets/roller-blackout.jpg" alt="Un store enrouleur occultant ordinaire avec des fentes de lumière visibles des deux côtés" />
          <figcaption>Un enrouleur occultant standard. Bon tissu — mais regardez la lumière des deux côtés.</figcaption>
        </figure>

        <h2>Ce qui rend le store Blockout différent</h2>
        <p>Le store Blockout installe un mince <strong>cadre</strong> d’aluminium autour de toute l’ouverture de la fenêtre. Le tissu occultant coulisse <em>à l’intérieur</em> de ce cadre dans des rails latéraux tendus, et le haut et le bas se scellent contre lui. Chaque bord est fermé — le haut, les deux côtés et le bas — alors la lumière n’a tout simplement nulle part où passer.</p>
        <ul>
          <li><strong>Cadre scellé</strong> — les bords du tissu logent dans les rails ; aucune fente latérale, aucune fente au bas.</li>
          <li><strong>Tendu, sans cordon</strong> — tirez la barre du bas et elle reste exactement où vous la laissez. Ni cordon ni chaînette — sécuritaire pour les enfants par conception.</li>
          <li><strong>Haut-bas ou bas-haut</strong> — abaissez-le par le haut pour laisser entrer un peu de lumière, ou fermez-le complètement.</li>
          <li><strong>Pose intérieure ou extérieure</strong> — l’intérieure exige environ 2,5 cm (1 po) de profondeur d’embrasure ; l’extérieure, environ 7,5 cm (3 po) de surface plane.</li>
          <li><strong>Options motorisées et intelligentes</strong> — programmez-le, commandez-le par appli ou par la voix.</li>
          <li><strong>Plus silencieux et plus frais</strong> — le tissu scellé atténue aussi le bruit extérieur et réduit le gain de chaleur estival.</li>
        </ul>
        <figure>
          <img src="../assets/blockout-sleep.jpg" alt="Une personne qui dort profondément dans une chambre sombre équipée d’un store Blockout" />
          <figcaption>Le résultat : une chambre noire à 6 h du matin en juin.</figcaption>
        </figure>

        <h2>Pour qui c’est fait</h2>
        <ul>
          <li><strong>Bébés et tout-petits</strong> — siestes et couchers tôt en saison lumineuse. Voyez notre <a href="blackout-blinds-for-nursery.html">guide chambre de bébé</a>.</li>
          <li><strong>Travailleurs de nuit et couche-tard</strong> — un vrai sommeil à 10 h.</li>
          <li><strong>Dormeurs légers et migraineux</strong>.</li>
          <li><strong>Cinémas maison et salles de jeu</strong>.</li>
          <li><strong>Quiconque vit dans un condo lumineux</strong> avec lampadaires et fenêtres des voisins.</li>
        </ul>

        <h2>Avantages et inconvénients, honnêtement</h2>""",
 pros=["<strong>Vraiment 100 % noir</strong> — le cadre scelle chaque bord ; ni halo ni barres de lumière.", "<strong>Sans cordon et sécuritaire pour les enfants</strong> — une barre tendue, rien qui pend.", "<strong>Flexibilité haut-bas / bas-haut.</strong>", "<strong>Pièce plus silencieuse et plus fraîche</strong> grâce au scellage.", "<strong>Motorisé et prêt pour la maison intelligente.</strong>", "<strong>Fait sur mesure</strong> pour chaque fenêtre."],
 cons=["<strong>Le cadre est visible</strong> — mince et soigné, mais on le voit autour de la fenêtre. Choisissez le fini assorti à vos moulures.", "<strong>Coûte plus qu’un enrouleur occultant ordinaire</strong> — vous payez pour le cadre et le scellage, et c’est exactement ce qui donne la noirceur.", "<strong>Exige un peu de profondeur ou de surface plane</strong> pour poser le cadre — on vérifie à la consultation.", "<strong>La noirceur totale n’est pas pour les salons</strong> — là, un <a href='roller-blinds.html'>enrouleur</a> tamisant ou un <a href='day-and-night-zebra-blinds.html'>store zébré</a>."],
 glance=[("Noirceur", (5, "100 % — cadre scellé")), ("Intimité", (5, "Absolue")), ("Isolation", (4, "Bonne ; les bords scellés aident")), ("Bruit", (4, "Nettement plus silencieux")), ("Style", (3, "Propre ; cadre visible")), ("Pièces idéales", "Chambres, chambres de bébé, cinémas maison, chambres de travailleurs de nuit, condos lumineux"), ("Options", "Pose intérieure / extérieure · haut-bas/bas-haut · sans cordon · motorisé · finis du cadre")],
 body2="""
        <div class="callout"><strong>Store Blockout ou enrouleur occultant + rails latéraux ?</strong><p>On peut s’approcher de la noirceur totale en ajoutant des rails latéraux à un enrouleur occultant — on le fait souvent. Le store Blockout en est la version conçue exprès : le cadre <em>est</em> le système de rails, haut et bas compris, en un seul ensemble propre. Si la noirceur est toute la raison d’être de la pièce, c’est celui-là.</p></div>
        <h2>Quand choisir autre chose</h2>
        <ul>
          <li>Vous voulez la noirceur <em>et</em> une isolation maximale sur une fenêtre froide ? Un <a href="honeycomb-blinds.html">alvéolaire</a> occultant avec rails.</li>
          <li>Vous préférez un look doux et décoratif ? Des <a href="curtains-and-drapes.html">rideaux</a> doublés occultants ou un <a href="roman-shades.html">store bateau</a> (attendez-vous à un peu de lumière sur les bords).</li>
        </ul>""",
 faq=[("Le store Blockout est-il vraiment occultant à 100 % ?", "Oui. Contrairement à un store occultant ordinaire, le tissu coulisse à l’intérieur d’un cadre qui scelle le haut, les deux côtés et le bas de la fenêtre, alors il n’y a aucun bord par où la lumière peut fuir."),
      ("Quelle est la différence entre un store Blockout et un enrouleur occultant ?", "Un enrouleur occultant utilise un tissu opaque mais pend avec de petites fentes sur les côtés par où la lumière entre. Un store Blockout place le tissu dans un cadre scellé avec des rails latéraux tendus — aucune fente."),
      ("Est-il sécuritaire pour les enfants ?", "Oui — il est sans cordon. On déplace une barre du bas tendue ; il n’y a ni cordon ni chaînette."),
      ("Peut-on le motoriser ?", "Oui, avec commande par appli, par la voix et par horaire — une belle combinaison pour une chambre qui s’ouvre doucement à votre heure de réveil."),
      ("Convient-il à ma fenêtre ?", "La pose intérieure exige environ 2,5 cm de profondeur d’embrasure ; la pose extérieure, environ 7,5 cm de surface plane autour de la fenêtre. On le confirme à votre consultation gratuite."),
      ("Est-ce que vous l’installez ?", "Oui — mesuré, fabriqué à la taille et installé gratuitement partout à Montréal.")],
 aside_h="Voyez un store Blockout en personne", aside_p="Consultation gratuite à domicile. Nous apportons un échantillon pour que vous voyiez le cadre et le scellage, et vérifions la profondeur de votre fenêtre.",
 cta_h="Dormez comme s’il était <em>minuit</em> à midi.", cta_p="Réservez une consultation gratuite. Nous mesurons, confirmons la pose et installons gratuitement.",
 related=[R["nursery"], R["honey"], R["motor"]]),

# ---------------------------------------------------------------- OUTDOOR
dict(slug="outdoor-blinds.html", type="guide", crumb="Stores extérieurs", read=5, image=IMG["outdoor"],
 alt="Un patio extérieur couvert avec des stores résistants aux intempéries",
 title="Stores extérieurs pour patios et balcons : fonctionnement, avantages, inconvénients",
 description="Les stores extérieurs expliqués : tissus résistants aux intempéries, systèmes à glissières (zip) et à câbles, résistance au vent et au soleil, avantages et inconvénients honnêtes, et comment ils gèrent les saisons montréalaises. Installés gratuitement.",
 og="Prolongez votre espace de vie dehors — de l’ombre résistante aux intempéries qui gère les saisons montréalaises.",
 h1="Stores extérieurs : faites de votre patio une <em>pièce</em> de plus.",
 lede="De l’ombre contre le soleil de l’après-midi, un abri contre la brise, de l’intimité vis-à-vis des voisins — les stores extérieurs rendent un balcon, une terrasse ou un patio utilisable beaucoup plus longtemps dans l’année. Voici en quoi les systèmes diffèrent et ce qui tient le coup dans notre climat.",
 body="""
        <h2>Qu’est-ce qu’un store extérieur ?</h2>
        <p>Des stores enrouleurs d’extérieur faits de <strong>toiles maillées ou de PVC résistants aux intempéries</strong>, fixés à une pergola, une ouverture de balcon, une couverture de patio ou l’extérieur d’une fenêtre. Baissez-les pour couper le soleil et l’éblouissement, bloquer le vent et ajouter de l’intimité ; relevez-les pour ouvrir l’espace complètement.</p>

        <h2>Comment ça fonctionne</h2>
        <h3>Les systèmes</h3>
        <ul>
          <li><strong>Stores à glissières (zip)</strong> — les bords de la toile coulissent dans des rails latéraux, de sorte que le store reste tendu, scellé et stable même au vent. L’option haut de gamme, la plus résistante aux intempéries, et celle que nous recommandons pour les balcons ouverts et les pergolas.</li>
          <li><strong>À câbles</strong> — le store coulisse sur des câbles tendus ; plus léger et plus économique, idéal pour les endroits abrités.</li>
          <li><strong>Stores de fenêtre extérieurs</strong> — un enrouleur d’extérieur posé sur la face externe d’une fenêtre pour arrêter la chaleur avant qu’elle n’atteigne la vitre — la façon la plus efficace de garder fraîche une pièce ensoleillée.</li>
        </ul>
        <h3>Les toiles</h3>
        <ul>
          <li><strong>Toile solaire maillée</strong> — bloque la plupart des UV et de l’éblouissement tout en gardant la vue et la circulation d’air. Le choix de tous les jours.</li>
          <li><strong>PVC clair / teinté</strong> — une barrière contre le vent et la pluie qui garde la vue ; l’effet « mur de verre ».</li>
          <li><strong>Opaque</strong> — intimité et ombre complètes.</li>
        </ul>
        <p>Manœuvre par manivelle, ressort ou — très populaire dehors — <strong>moteur</strong> avec capteur de vent qui relève automatiquement le store en cas de bourrasque.</p>

        <h2>Avantages et inconvénients, honnêtement</h2>""",
 pros=["<strong>Rend l’espace extérieur utilisable</strong> par beaucoup plus de temps.", "<strong>Coupe la chaleur et l’éblouissement</strong> avant qu’ils n’atteignent vos fenêtres et vos meubles.", "<strong>Intimité</strong> vis-à-vis des voisins et de la rue.", "<strong>Abri contre le vent et la pluie légère</strong> avec les glissières et le PVC.", "<strong>Motorisé avec capteurs de vent</strong> pour une protection sans intervention.", "<strong>Protège les meubles d’extérieur</strong> des UV."],
 cons=["<strong>Les hivers montréalais</strong> — la plupart des toiles extérieures devraient être relevées lors de fortes neiges et de glace ; on vous conseille sur l’usage saisonnier.", "<strong>Exige des points de fixation solides</strong> — une pergola, des poteaux ou une poutre ; tous les balcons n’en ont pas.", "<strong>Les règlements de copropriété</strong> peuvent restreindre les installations extérieures — vérifiez d’abord (on peut aider).", "<strong>Coûte plus qu’un store intérieur</strong> — la quincaillerie extérieure est plus robuste.", "<strong>Nettoyage</strong> — arroser périodiquement au boyau."],
 glance=[("Soleil et éblouissement", (5, "Excellent")), ("Abri contre le vent", (4, "Glissières / PVC")), ("Intimité", (4, "Du maillé à l’opaque")), ("Usage hivernal", (2, "Relever en cas de neige / glace")), ("Entretien", (3, "Arroser au boyau")), ("Idéal pour", "Patios, pergolas, balcons, terrasses, fenêtres ensoleillées"), ("Options", "Glissières · câbles · store de fenêtre extérieur · maillé / PVC / opaque · manivelle / moteur / capteur de vent")],
 body2="""
        <h2>Pour qui c’est parfait</h2>
        <p><strong>Si vous avez un patio, une terrasse ou un balcon que vous n’utilisez pas autant que vous le voudriez à cause du soleil, du vent ou des voisins — ça règle le problème.</strong> Les stores extérieurs sont aussi la réponse la plus intelligente pour une pièce qui surchauffe l’été : ombrager la vitre de l’<em>extérieur</em> est bien plus efficace que n’importe quel store intérieur.</p>
        <div class="callout"><strong>Réalité montréalaise</strong><p>Ici, les stores extérieurs sont une amélioration trois saisons. Nous spécifions des toiles et des fixations pour notre gel-dégel et vous conseillons sur le moment de les relever pour l’hiver — la plupart des clients gagnent de mai à octobre d’espace de vie en plus, exactement quand ils le veulent.</p></div>""",
 faq=[("Les stores extérieurs survivent-ils aux hivers montréalais ?", "La quincaillerie, oui ; la toile devrait généralement être relevée lors de fortes neiges et de glace. Nous spécifions des systèmes pour notre climat et vous conseillons sur l’usage saisonnier — voyez-les comme une amélioration trois saisons."),
      ("Puis-je installer des stores extérieurs sur un balcon de condo ?", "Souvent oui, mais beaucoup d’immeubles restreignent les installations extérieures. Vérifiez d’abord vos règlements — nous sommes heureux de vous aider à présenter la demande."),
      ("Glissières ou câbles : lequel est mieux ?", "Glissières pour les espaces ouverts, venteux ou exposés — elles scellent les bords et gardent la toile tendue. Câbles pour les endroits abrités et les budgets plus serrés."),
      ("Peut-on motoriser les stores extérieurs ?", "Oui, et c’est notre recommandation habituelle dehors — jumelez-les à un capteur de vent pour qu’ils se relèvent automatiquement en cas de fortes rafales."),
      ("Est-ce que vous les installez ?", "Oui — nous relevons vos points de fixation, spécifions le bon système et installons gratuitement partout à Montréal.")],
 aside_h="Obtenez une visite sur place", aside_p="Consultation gratuite. Nous examinons votre patio ou balcon, vérifions les points de fixation et les règlements, et recommandons le bon système.",
 cta_h="Votre patio, <em>trois saisons</em> par année.", cta_p="Réservez une consultation gratuite. Nous relevons l’espace, spécifions le système et installons gratuitement.",
 related=[R["roller"], R["motor"], R["condo"]]),

# ---------------------------------------------------------------- SMART FILM
dict(slug="smart-film.html", type="guide", crumb="Film intelligent", read=5, image=IMG["film"],
 alt="Une cloison vitrée — le genre de surface sur laquelle on applique le film intelligent commutable",
 title="Film intelligent : une vitre d’intimité d’une simple pression (fonctionnement, avantages, inconvénients)",
 description="Le film intelligent commutable expliqué : comment le film PDLC rend le verre clair ou dépoli instantanément, où on l’utilise (salles de bain, bureaux, cloisons, vitrines), avantages et inconvénients, et installation à Montréal.",
 og="Un film commutable qui rend le verre clair ou dépoli — comment ça fonctionne et où c’est génial.",
 h1="Film intelligent : une vitre d’intimité d’une simple <em>pression.</em>",
 lede="Clair un instant, dépoli l’instant d’après. Le film intelligent transforme n’importe quelle vitre existante en verre d’intimité commutable — pas de stores, pas de rideaux, rien à nettoyer. C’est la chose la plus futuriste que nous installions, et c’est étonnamment pratique.",
 body="""
        <h2>Qu’est-ce que le film intelligent ?</h2>
        <p>Un film mince et autocollant appliqué sur le verre. À l’intérieur, une couche de <strong>PDLC</strong> (cristaux liquides dispersés dans un polymère). Hors tension, les cristaux diffusent la lumière et le verre paraît <strong>dépoli</strong> — complètement privé. Appliquez un faible courant et les cristaux s’alignent : le verre devient <strong>clair</strong> instantanément. Un interrupteur, une télécommande, une appli ou une commande vocale.</p>

        <h2>Comment ça fonctionne</h2>
        <p>Nous appliquons le film sur votre verre existant (fenêtres, portes, cloisons, parois de douche, vitrines) et le relions à un petit transformateur. Commande par :</p>
        <ul>
          <li><strong>Interrupteur mural</strong> — le plus simple.</li>
          <li><strong>Télécommande ou appli</strong> — y compris les horaires.</li>
          <li><strong>Voix / maison intelligente</strong> — « rends le bureau privé ».</li>
        </ul>
        <p>Le dépoli est l’état <em>par défaut</em> (hors tension), donc l’intimité est garantie même en cas de panne. En mode clair, le film est très transparent avec un léger voile — comme un très bon verre. Il bloque aussi la plupart des UV.</p>
        <figure>
          <img src="../assets/smartfilm-before-after.jpg" alt="Film intelligent sur un vitrage latéral de porte d’entrée : dépoli avec l’intimité activée, et clair avec l’intimité désactivée" />
          <figcaption>Une de nos installations — un vitrage latéral de porte d’entrée. Intimité activée (dépoli) et désactivée (clair), même vitre.</figcaption>
        </figure>

        <h2>Là où c’est génial</h2>
        <ul>
          <li><strong>Salles de bain et salles d’eau attenantes</strong> — parois de douche et fenêtres vitrées qui deviennent privées sur demande.</li>
          <li><strong>Bureaux à domicile et salles de réunion</strong> — ouverts quand vous voulez du lien, privés pour un appel.</li>
          <li><strong>Cloisons vitrées</strong> — gardez la lumière, contrôlez la vue.</li>
          <li><strong>Vitrines et cliniques</strong> — intimité après les heures d’ouverture ou entre les clients.</li>
          <li><strong>Projection</strong> — en mode dépoli, le film sert aussi d’écran de rétroprojection.</li>
        </ul>

        <h2>Avantages et inconvénients, honnêtement</h2>""",
 pros=["<strong>Intimité instantanée</strong> — pas de stores, pas de rideaux, rien qui gêne.", "<strong>Garde la lumière</strong> même en mode privé (le dépoli reste lumineux).", "<strong>Zéro nettoyage</strong> — c’est juste du verre.", "<strong>Fonctionne sur le verre existant</strong> — pas besoin de remplacer les fenêtres.", "<strong>Privé par défaut</strong> — sécuritaire en cas de panne.", "<strong>Bloque les UV</strong> ; peut servir d’écran de projection.", "<strong>Prêt pour la maison intelligente.</strong>"],
 cons=["<strong>Pas un occultant</strong> — le dépoli diffuse la lumière, il ne la bloque pas. Pour la noirceur, voyez le <a href='blackout-blinds.html'>store Blockout</a>.", "<strong>A besoin d’électricité</strong> — un transformateur basse tension et un fil discret jusqu’au verre.", "<strong>Coûte plus au mètre carré</strong> qu’un store.", "<strong>Léger voile en mode clair</strong> — à peine perceptible, mais pas invisible.", "<strong>Aucune isolation thermique</strong> notable."],
 glance=[("Intimité", (5, "Instantanée, totale")), ("Lumière", (5, "Conservée dans les deux modes")), ("Noirceur", (1, "Aucune — pas occultant")), ("Style", (5, "Élégant, invisible")), ("Entretien", (5, "C’est du verre")), ("Idéal pour", "Salles de bain, bureaux, cloisons, vitrines, cliniques"), ("Options", "Interrupteur mural · télécommande · appli · voix · horaires · projection")],
 body2="""
        <div class="callout"><strong>Résidentiel et commercial</strong><p>Nous installons le film intelligent dans les maisons — le plus souvent salles de bain et bureaux à domicile — et dans les bureaux, cliniques et commerces partout à Montréal. Montrez-nous la vitre ; nous vous dirons exactement ce qui est possible.</p></div>""",
 faq=[("Le film intelligent est-il privé la nuit avec les lumières allumées ?", "Oui — en mode dépoli, on ne voit pas à travers, d’aucun côté, jour ou nuit. Les silhouettes ne sont pas visibles comme elles le sont à travers un voile."),
      ("Le film intelligent a-t-il besoin d’électricité en permanence ?", "Seulement pour être clair. Le dépoli (privé) est l’état hors tension, donc il ne consomme que pendant que vous voulez la transparence, et reste privé en cas de panne."),
      ("Peut-on l’appliquer sur ma paroi de douche / ma fenêtre existante ?", "Dans la plupart des cas oui — il s’applique sur le verre existant. Nous vérifions le type de verre et les bords lors d’une consultation."),
      ("Est-ce occultant ?", "Non. Il donne de l’intimité tout en laissant passer une lumière diffuse. Pour la noirceur, jumelez-le à un store ou un rideau occultant."),
      ("Est-ce que vous l’installez ?", "Oui — nous évaluons le verre, installons le film et le transformateur, et relions les commandes de votre choix, partout à Montréal.")],
 aside_h="Voyez-le commuter, en personne", aside_p="Consultation gratuite. Nous évaluons votre verre et vous montrons un échantillon fonctionnel.",
 cta_h="Clair. Dépoli. <em>À vous de choisir.</em>", cta_p="Réservez une consultation gratuite. Nous vérifions votre verre et vous donnons un prix sur place.",
 related=[R["blackout"], R["condo"], R["motor"]]),

# ================================================================ CONSEILS / SEO
dict(slug="blinds-vs-curtains.html", type="advice", crumb="Stores ou rideaux", read=6, image=IMG["living"],
 alt="Un salon avec des habillages de fenêtre superposés",
 title="Stores ou rideaux : lequel convient à votre pièce ? (guide pièce par pièce)",
 description="Stores ou rideaux ? Une comparaison pratique pièce par pièce — lumière, intimité, isolation, nettoyage, style et coût — et pourquoi les plus belles maisons superposent souvent les deux. Conseils d’un atelier de stores sur mesure de Montréal.",
 og="Une réponse pièce par pièce, et pourquoi les plus belles maisons utilisent souvent les deux.",
 h1="Stores ou rideaux : lequel convient à <em>votre</em> pièce ?",
 lede="C’est la première question que presque tout le monde nous pose — et la réponse honnête, c’est « ça dépend de la pièce ». Voici la comparaison claire, puis le verdict pièce par pièce, puis le truc des designers : les deux.",
 body="""
        <h2>La comparaison rapide</h2>
        <table class="specs">
          <tr><th></th><td><strong>Stores</strong></td></tr>
          <tr><th>Look</th><td>Propre, ajusté, minimaliste. Disparaissent une fois relevés.</td></tr>
          <tr><th>Contrôle de la lumière</th><td>Précis — du voile à l’occultant ; les zébrés et les lattes se règlent par degrés.</td></tr>
          <tr><th>Isolation</th><td>Alvéolaire : excellente. Enrouleur/zébré : modeste.</td></tr>
          <tr><th>Nettoyage</th><td>Facile — dépoussiérer ou essuyer.</td></tr>
          <tr><th>Pièces humides</th><td>Oui — tissus faciles d’entretien.</td></tr>
          <tr><th>Coût</th><td>Généralement plus bas par fenêtre.</td></tr>
        </table>
        <table class="specs">
          <tr><th></th><td><strong>Rideaux</strong></td></tr>
          <tr><th>Look</th><td>Doux, chaleureux, dramatique. Font paraître les plafonds plus hauts.</td></tr>
          <tr><th>Contrôle de la lumière</th><td>Ouverts ou fermés ; voiles pour tamiser, doublure occultante pour la noirceur.</td></tr>
          <tr><th>Isolation</th><td>Très bonne avec doublure ; absorbent aussi le son.</td></tr>
          <tr><th>Nettoyage</th><td>Périodique ; selon le tissu.</td></tr>
          <tr><th>Pièces humides</th><td>Pas idéal.</td></tr>
          <tr><th>Coût</th><td>Plus de tissu + doublure, donc habituellement plus élevé.</td></tr>
        </table>

        <h2>Pièce par pièce</h2>
        <h3>Salon</h3>
        <p><strong>Les deux.</strong> Un rideau voile ou un <a href="day-and-night-zebra-blinds.html">store zébré</a> pour la lumière et l’intimité le jour, avec des rideaux pour la chaleur et les soirées. S’il faut n’en choisir qu’un : des rideaux pour une pièce douce et finie ; un store zébré pour une pièce moderne avec beaucoup de vitres.</p>
        <h3>Chambre</h3>
        <p><strong>L’occultant est la priorité</strong> — un <a href="blackout-blinds.html">store occultant avec rails latéraux</a> fait le travail le mieux, et des rideaux doublés occultants par-dessus donnent le look hôtel. Pièce froide ? <a href="honeycomb-blinds.html">Alvéolaire occultant</a>.</p>
        <h3>Cuisine et salle de bain</h3>
        <p><strong>Des stores.</strong> Un <a href="roller-blinds.html">enrouleur</a> facile d’entretien ou un <a href="roman-shades.html">store bateau</a> en tissu lavable. Rideaux et vapeur/éclaboussures ne font pas bon ménage. Salle de bain avec douche vitrée ? Pensez au <a href="smart-film.html">film intelligent</a>.</p>
        <h3>Bureau à domicile</h3>
        <p><strong>Des stores</strong> — le contrôle de l’éblouissement compte le plus sur un écran. Un zébré ou un enrouleur tamisant ; alvéolaire si la fenêtre est froide.</p>
        <h3>Salle à manger</h3>
        <p><strong>Rideaux ou stores bateau</strong> — de la douceur et un peu d’occasion.</p>
        <h3>Chambre d’enfant / de bébé</h3>
        <p><strong>Store occultant sans cordon</strong> — sécurité et sommeil. Voyez le <a href="blackout-blinds-for-nursery.html">guide chambre de bébé</a>.</p>
        <h3>Porte-patio / très grande fenêtre</h3>
        <p><strong>Rideaux sur rail</strong> ou un <a href="roller-blinds.html">enrouleur</a>/zébré large. Les stores bateau deviennent lourds au-delà d’environ 2 m.</p>

        <h2>La réponse des designers : superposez-les</h2>
        <p>Parcourez n’importe quelle maison bien conçue et vous remarquerez que la plupart des fenêtres ont <em>deux</em> habillages : une couche fonctionnelle pour la lumière et l’intimité (un store ou un voile) et une couche décorative pour la douceur (des rideaux). Vous obtenez un contrôle précis le jour et de la chaleur le soir — et ça photographie superbement. Ça n’a pas à coûter cher : un simple enrouleur ou alvéolaire derrière une paire de rideaux doublés, c’est un classique.</p>
        <div class="callout"><strong>Notre règle d’or honnête</strong><p>Pièce humide ou très sollicitée → store. Pièce où vous vous détendez → rideaux (ou les deux). Chambre → occultant d’abord, style ensuite. Fenêtre froide → alvéolaire, peu importe ce que vous ajoutez.</p></div>""",
 pros=None, cons=None, glance=None, body2="",
 faq=[("Stores ou rideaux : lequel isole le mieux ?", "Les rideaux doublés isolent bien ; les stores alvéolaires (cellulaires) isolent le mieux de tous les habillages seuls. Combiner un store alvéolaire avec des rideaux doublés est l’option la plus chaude de toutes."),
      ("Stores ou rideaux : lequel est le moins cher ?", "Les stores sont généralement moins chers par fenêtre ; les rideaux utilisent plus de tissu plus la doublure. Superposer les deux coûte plus mais remplace souvent le besoin d’un habillage unique haut de gamme."),
      ("Puis-je avoir des stores et des rideaux sur une même fenêtre ?", "Oui — c’est l’approche classique des designers. Un store ou un voile pour la fonction, des rideaux pour la douceur. Nous faisons cette combinaison constamment."),
      ("Qu’est-ce qui est le mieux pour une chambre ?", "L’occultant. Un store occultant avec rails latéraux pour une vraie noirceur, éventuellement avec des rideaux doublés occultants par-dessus. Ajoutez l’alvéolaire si la pièce est froide."),
      ("Faites-vous les stores et les rideaux ?", "Oui — tout sur mesure, et nous installons tout gratuitement partout à Montréal.")],
 aside_h="Pas certain ? On vous le dira honnêtement", aside_p="Consultation gratuite à domicile. Nous regardons chaque pièce et recommandons stores, rideaux ou les deux — avec des échantillons.",
 cta_h="Stores, rideaux, ou <em>les deux</em> — décidé dans votre salon.", cta_p="Réservez une consultation gratuite. Nous apportons des échantillons de tout et vous donnons une réponse franche, pièce par pièce.",
 related=[R["curtains"], R["roller"], R["honey"]]),

dict(slug="best-blinds-for-montreal-winters.html", type="advice", crumb="Stores pour l’hiver montréalais", read=6, image=IMG["bedroom"],
 alt="Une chambre douillette dans la douce lumière d’hiver",
 title="Les meilleurs stores pour l’hiver montréalais (et des factures de chauffage plus basses)",
 description="Les fenêtres perdent une quantité surprenante de chaleur. Voici ce qui aide vraiment durant un hiver montréalais, classé — stores alvéolaires, rideaux doublés, superposition, et les détails de pose qui comptent — par un atelier local de stores sur mesure.",
 og="Les fenêtres perdent une quantité surprenante de chaleur — voici ce qui aide vraiment, classé.",
 h1="Les meilleurs stores pour l’hiver montréalais — <em>classés.</em>",
 lede="Tenez-vous à côté d’une fenêtre en janvier et vous le sentez : le froid qui coule de la vitre. Les fenêtres sont le maillon faible de l’isolation d’une maison, et le bon habillage de fenêtre fait une différence réelle et perceptible. Voici ce qui fonctionne, dans l’ordre.",
 body="""
        <h2>Pourquoi les fenêtres comptent autant</h2>
        <p>Même un bon double vitrage isole bien moins qu’un mur isolé. Une grande fenêtre ou une fenêtre ancienne peut être responsable d’une large part de la perte de chaleur d’une pièce — c’est pour ça que la zone près de la vitre est froide et que votre chauffage travaille plus fort. Un habillage qui emprisonne de l’air immobile contre la vitre ralentit cette perte.</p>

        <h2>Classement : ce qui aide vraiment</h2>
        <h3>1. Stores alvéolaires (cellulaires) — le gagnant</h3>
        <p>Les stores cellulaires emprisonnent l’air dans des rangées de poches fermées, et l’air immobile conduit mal la chaleur. Rien d’autre dans le monde des stores n’approche ça. L’alvéolaire <strong>double</strong> double encore à peu près l’effet — c’est le choix pour les fenêtres les plus froides. Posez-les <em>à l’intérieur</em> du cadre, près de la vitre, pour que la couche emprisonnée soit scellée. Lisez le <a href="honeycomb-blinds.html">guide alvéolaire</a> complet.</p>
        <h3>2. Rideaux doublés — un proche second, et plus chaleureux au ressenti</h3>
        <p>Des rideaux lourds, <strong>doublés thermiques</strong>, qui tombent au plancher et chevauchent généreusement la fenêtre créent une grande poche d’air immobile. Ils absorbent aussi le son et rendent une pièce douillette. Les détails comptent : longueur au plancher, chevauchement large, et idéalement un rail à retour pour sceller les côtés. Voyez <a href="curtains-and-drapes.html">rideaux et draperies</a>.</p>
        <h3>3. Superposez les deux — l’option la plus chaude de toutes</h3>
        <p>Un store alvéolaire contre la vitre avec des rideaux doublés devant. Deux couches d’air emprisonné, un confort maximal, et on dirait qu’un designer est passé. C’est ce que nous recommandons pour les chambres froides et les grandes fenêtres de salon.</p>
        <h3>4. Stores bateau, doublés</h3>
        <p>Un store bateau doublé aide de façon notable — plus qu’un enrouleur, moins qu’un alvéolaire — et il est très beau.</p>
        <h3>5. Stores enrouleurs et zébrés — modeste</h3>
        <p>Une seule couche de tissu avec des fentes sur les côtés n’emprisonne pas beaucoup d’air. Utiles quand même pour l’intimité et l’éblouissement, et les tissus occultants/thermiques aident un peu — mais si la chaleur est l’objectif, choisissez l’alvéolaire.</p>

        <h2>Les détails qui font que ça marche</h2>
        <ul>
          <li><strong>Posez près de la vitre</strong> — une pose intérieure avec un minimum de fentes scelle la couche d’air.</li>
          <li><strong>Fermez-les au crépuscule</strong> — la plupart de la chaleur se perd la nuit ; ouvrez les jours ensoleillés pour capter la chaleur solaire gratuite, surtout au sud.</li>
          <li><strong>Des rails latéraux</strong> sur un alvéolaire ou un occultant scellent les bords — meilleure isolation <em>et</em> noirceur.</li>
          <li><strong>Automatisez</strong> — des stores <a href="motorized-blinds.html">motorisés</a> sur un horaire coucher/lever du soleil s’occupent de la fermeture pour vous.</li>
        </ul>
        <div class="callout"><strong>Ce que nos clients nous disent</strong><p>Le commentaire le plus fréquent après l’installation de stores alvéolaires dans une vieille maison montréalaise, c’est une variante de « la pièce a juste l’air plus chaude ». Ce n’est pas une impression — c’est le courant froid de la vitre qui est interrompu.</p></div>""",
 pros=None, cons=None, glance=None, body2="",
 faq=[("Quels sont les stores les plus chauds ?", "Les stores alvéolaires (cellulaires) — double alvéole pour les fenêtres les plus froides — posés près de la vitre. Superposez des rideaux doublés par-dessus pour un effet maximal."),
      ("Les stores réduisent-ils vraiment les factures de chauffage ?", "Ils réduisent la perte de chaleur par la vitre, donc votre chauffage tourne moins pour maintenir la même température. L’effet est le plus grand sur les fenêtres grandes, anciennes ou au nord, et le plus perceptible en confort près de la fenêtre."),
      ("Les rideaux sont-ils plus chauds que les stores ?", "Des rideaux doublés thermiques, longueur plancher, sont très chauds — comparables à un bon store alvéolaire. Ensemble, ils battent l’un ou l’autre seul."),
      ("Les stores doivent-ils être ouverts ou fermés l’hiver ?", "Fermés la nuit et les jours gris pour garder la chaleur ; ouverts les jours ensoleillés (surtout au sud) pour laisser entrer la chaleur solaire gratuite. Un horaire motorisé rend ça automatique."),
      ("Installez-vous des stores alvéolaires à Montréal ?", "Oui — sur mesure et installés gratuitement partout sur l’île et dans les environs.")],
 aside_h="Réchauffez la pièce froide", aside_p="Consultation gratuite à domicile. Nous vérifions vos fenêtres et recommandons la bonne combinaison pour un vrai confort hivernal.",
 cta_h="Sentez la différence <em>cet</em> hiver.", cta_p="Réservez une consultation gratuite. Nous mesurons, apportons des échantillons d’alvéolaire et de doublure, et installons gratuitement.",
 related=[R["honey"], R["curtains"], R["motor"]]),

dict(slug="blackout-blinds-for-nursery.html", type="advice", crumb="Occultant pour la chambre de bébé", read=5, image=IMG["calm"],
 alt="Une pièce calme et minimaliste dans une lumière douce",
 title="Stores occultants pour la chambre de bébé : le guide des parents pour de meilleures siestes",
 description="Choisir des stores occultants pour la chambre d’un bébé : sécurité sans cordon, vraie noirceur (rails latéraux), tissus faciles d’entretien, isolation et options motorisées silencieuses. Conseils pratiques d’un atelier de stores sur mesure de Montréal.",
 og="Sécurité, noirceur et durabilité — ce qu’il faut chercher quand l’objectif est le sommeil.",
 h1="Stores occultants pour la chambre de bébé : le guide des parents pour de <em>meilleures siestes.</em>",
 lede="Une pièce sombre, c’est l’une des rares choses du sommeil de bébé qui dépend vraiment de vous. Voici comment obtenir une vraie noirceur en toute sécurité — et les détails que les parents nous disent avoir aimé connaître avant.",
 body="""
        <h2>Les quatre choses qui comptent</h2>
        <h3>1. Sans cordon. Toujours.</h3>
        <p>Les cordons et chaînettes pendants sont un risque d’étranglement pour les bébés et les tout-petits. Choisissez un fonctionnement <strong>sans cordon (ressort)</strong> ou <strong>motorisé</strong> — pas de boucles, rien à atteindre. C’est non négociable dans une chambre de bébé, et tout ce que nous recommandons ci-dessous est sans cordon.</p>
        <h3>2. Une vraie noirceur, pas « plutôt sombre »</h3>
        <p>Le tissu occultant seul laisse fuir la lumière sur les bords — des barres lumineuses à 5 h du matin. Pour une vraie noirceur, il vous faut un store occultant coulissant dans des <strong>rails latéraux</strong> (ou une généreuse pose extérieure, idéalement avec des rideaux occultants par-dessus). Lisez <a href="blackout-blinds.html">comment obtenir vraiment la noirceur totale</a>.</p>
        <h3>3. Facile à nettoyer</h3>
        <p>Les chambres de bébé, ça colle. Un <strong>enrouleur occultant</strong> en tissu lavable est le gagnant pratique. Si la pièce est froide, un <strong>alvéolaire occultant</strong> ajoute isolation et silence — dépoussiérez-le délicatement.</p>
        <h3>4. Un fonctionnement silencieux</h3>
        <p>Vous sortirez de cette pièce sur la pointe des pieds. Les ressorts sans cordon sont silencieux ; les bons moteurs sont ultra-silencieux et vous permettent d’ouvrir le store lentement selon un horaire pour que les matins soient doux plutôt que brusques.</p>

        <figure>
          <img src="../assets/honeycomb-kids.jpg" alt="Une chambre d’enfant avec un store alvéolaire haut-bas — lumière par le voile en haut, cellules occultantes en bas" />
          <figcaption>Une vraie chambre d’enfant de chez nous : alvéolaire haut-bas, la lumière entre en haut pendant que la moitié inférieure reste couverte.</figcaption>
        </figure>
        <h2>Notre recommandation pour la chambre de bébé</h2>
        <ul>
          <li><strong>Enrouleur occultant, sans cordon ou motorisé, avec rails latéraux</strong> — le scellage le plus étanche, le plus facile à nettoyer, le plus économique.</li>
          <li><strong>Alvéolaire occultant avec rails</strong> si la pièce est froide ou bruyante — noirceur plus isolation et amortissement du son.</li>
          <li><strong>En option :</strong> des rideaux doublés occultants par-dessus pour la douceur et un scellage supplémentaire — posez le rail haut et large, et gardez-les hors de portée d’un tout-petit debout.</li>
        </ul>
        <div class="callout"><strong>Petits détails qui aident</strong><p>Choisissez un tissu de face pâle ou à motifs pour que la pièce reste gaie le jour. Demandez un joint au bas. Et si vous motorisez, programmez une « ouverture lente » à l’heure du réveil — ça fonctionne étonnamment bien.</p></div>

        <h2>À éviter</h2>
        <ul>
          <li>Tout store à cordon ou chaînette à portée de main.</li>
          <li>Un occultant en pose intérieure sans rails — vous aurez des halos de lumière.</li>
          <li>Des rideaux lourds qu’un tout-petit peut tirer — ou fixez-les solidement et haut.</li>
        </ul>""",
 pros=None, cons=None, glance=None, body2="",
 faq=[("Les stores occultants sont-ils sécuritaires pour une chambre de bébé ?", "Oui, quand ils sont sans cordon (ressort) ou motorisés — aucun cordon ni chaînette pendante. Tout ce que nous recommandons pour les chambres de bébé est sans cordon."),
      ("Comment rendre une chambre de bébé complètement sombre ?", "Un store occultant coulissant dans des rails latéraux (avec un joint au bas), ou une pose extérieure avec un généreux chevauchement plus des rideaux occultants par-dessus. Le tissu occultant seul fuit sur les bords."),
      ("Enrouleur ou alvéolaire pour la chambre de bébé ?", "Enrouleur pour le nettoyage le plus facile et le meilleur rapport qualité-prix ; alvéolaire si la pièce est froide ou bruyante, parce qu’il ajoute isolation et silence."),
      ("Puis-je programmer le store pour s’ouvrir à l’heure du réveil ?", "Oui — les stores motorisés peuvent s’ouvrir lentement selon un horaire pour que les matins soient doux."),
      ("Est-ce que vous les installez ?", "Oui — mesurés, posés avec rails au besoin et installés gratuitement partout à Montréal.")],
 aside_h="Rendez la chambre de bébé vraiment sombre", aside_p="Consultation gratuite à domicile. Nous vérifions la fenêtre et spécifions un occultant sans cordon et scellé qui fonctionne vraiment.",
 cta_h="Les meilleures siestes commencent par une pièce plus <em>sombre.</em>", cta_p="Réservez une consultation gratuite. Sans cordon, scellé, facile d’entretien — mesuré et installé gratuitement.",
 related=[R["blackout"], R["honey"], R["motor"]]),

dict(slug="how-to-measure-windows-for-blinds.html", type="advice", crumb="Comment mesurer", read=6, image=IMG["measure"],
 alt="Mesure d’un cadre de fenêtre pour des stores sur mesure",
 title="Comment mesurer ses fenêtres pour des stores (pose intérieure ou extérieure, étape par étape)",
 description="Comment mesurer une fenêtre pour des stores : pose intérieure ou extérieure, la règle des trois largeurs, la profondeur pour les cassettes et les rails, les erreurs courantes — et pourquoi nous venons quand même mesurer pour vous, gratuitement, à Montréal.",
 og="Les étapes, les erreurs courantes — et pourquoi nous venons quand même mesurer pour vous.",
 h1="Comment mesurer ses fenêtres pour des stores — et les erreurs qui <em>gâchent</em> un ajustement.",
 lede="Des stores sur mesure n’ont l’air sur mesure que si les mesures sont exactes. Voici exactement comment on fait, pour que vous compreniez ce qu’exige un bon ajustement — et pourquoi, pour la vraie affaire, nous venons mesurer pour vous sans frais.",
 body="""
        <h2>D’abord, décidez : pose intérieure ou extérieure ?</h2>
        <h3>Pose intérieure</h3>
        <p>Le store loge <em>à l’intérieur</em> de l’embrasure de la fenêtre. Propre et ajusté ; met en valeur les moulures ; garde le rebord utilisable. Exige assez de <strong>profondeur</strong> pour le mécanisme (une cassette ou des rails latéraux en demandent plus) et une ouverture raisonnablement d’équerre. De petites fentes de lumière sur les côtés sont normales — ajoutez des rails pour l’occultant.</p>
        <h3>Pose extérieure</h3>
        <p>Le store se fixe sur le mur ou la moulure <em>par-dessus</em> l’ouverture, plus grand que la fenêtre. Cache un cadre hors d’équerre ou peu profond, fait paraître la fenêtre plus grande, et bloque mieux la lumière parce que le tissu chevauche l’ouverture. Le choix habituel pour les rideaux et les stores bateau, et pour l’occultant sans rails.</p>

        <h2>Mesurer une pose intérieure</h2>
        <ol>
          <li><strong>Largeur — mesurez trois fois.</strong> En haut, au milieu et en bas de l’embrasure. Les cadres sont rarement d’équerre. Utilisez la mesure la <em>plus étroite</em>.</li>
          <li><strong>Hauteur — mesurez trois fois.</strong> À gauche, au centre et à droite, du haut de l’embrasure au rebord. Utilisez la <em>plus longue</em> pour un store qui doit atteindre le rebord.</li>
          <li><strong>Profondeur.</strong> Mesurez la profondeur de l’embrasure. Chaque type de store exige une profondeur minimale pour une pose affleurante (une cassette ou des rails latéraux en demandent plus). Si c’est peu profond, optez pour la pose extérieure.</li>
          <li><strong>Vérifiez les obstacles</strong> — poignées, manivelles, carrelage, capteurs d’alarme.</li>
          <li><strong>Ne déduisez rien.</strong> Donnez la dimension exacte de l’ouverture ; le fabricant applique le jeu correct pour ce produit.</li>
        </ol>

        <h2>Mesurer une pose extérieure</h2>
        <ol>
          <li><strong>Largeur.</strong> Mesurez l’ouverture et ajoutez un chevauchement de chaque côté — typiquement 5 à 8 cm par côté (plus pour l’occultant).</li>
          <li><strong>Hauteur.</strong> Décidez où le haut se fixera (au-dessus du cadre) et où le bas doit s’arrêter (rebord, ou en dessous), et mesurez entre les deux.</li>
          <li><strong>Vérifiez que la surface de pose</strong> est plane et solide, et qu’il y a de la place au-dessus du cadre pour le rail supérieur.</li>
        </ol>

        <h2>Les erreurs courantes qu’on voit</h2>
        <ul>
          <li>Mesurer une seule fois, au milieu — puis découvrir que le haut est 8 mm plus étroit.</li>
          <li>Arrondir au centimètre le plus proche. Les millimètres comptent.</li>
          <li>Déduire le jeu soi-même, puis le fabricant déduit encore → des fentes.</li>
          <li>Oublier la profondeur — la cassette ne loge pas dans l’embrasure.</li>
          <li>Ignorer la poignée qui pivote dans le store.</li>
          <li>Utiliser un ruban de couture ou un ruban tordu — utilisez un ruban d’acier rigide.</li>
        </ul>

        <div class="callout"><strong>Le fond de l’histoire</strong><p>Vous n’avez rien de tout ça à faire. Chaque commande My Kurtains comprend une <strong>prise de mesures gratuite à domicile</strong> par les gens qui vont l’installer — nous prenons la responsabilité de l’ajustement. Ce guide est là pour que vous compreniez ce que « sur mesure » veut vraiment dire, et pour que vous puissiez vérifier le travail de n’importe qui d’autre.</p></div>""",
 pros=None, cons=None, glance=None, body2="",
 faq=[("Est-ce que je mesure la fenêtre ou la taille du store ?", "Donnez la dimension exacte de l’ouverture (pour la pose intérieure) et laissez le fabricant faire les déductions pour ce produit précis — ne déduisez jamais vous-même, sinon vous déduirez deux fois et aurez des fentes."),
      ("Pose intérieure ou extérieure : laquelle est mieux ?", "Intérieure pour un look propre et ajusté si vous avez la profondeur et un cadre d’équerre. Extérieure pour cacher une embrasure hors d’équerre ou peu profonde, faire paraître la fenêtre plus grande, ou améliorer le blocage de la lumière."),
      ("Combien de chevauchement pour une pose extérieure ?", "Typiquement 5 à 8 cm de chaque côté et au-dessus du cadre ; plus si vous voulez l’occultant sans rails latéraux."),
      ("Pourquoi mesurer la largeur à trois endroits ?", "Parce que les embrasures de fenêtre sont rarement parfaitement d’équerre. Utiliser la mesure la plus étroite garantit que le store s’ajuste partout."),
      ("Est-ce que vous mesurez pour moi ?", "Oui — une prise de mesures gratuite à domicile est incluse avec chaque commande partout à Montréal, faite par nos installateurs.")],
 aside_h="Rangez le ruban à mesurer", aside_p="Prise de mesures et consultation gratuites à domicile. Nous mesurons chaque fenêtre nous-mêmes et garantissons l’ajustement.",
 cta_h="Sur mesure, ça veut dire que <em>nous</em> mesurons.", cta_p="Réservez une consultation gratuite. Nous venons chez vous, mesurons avec précision et installons gratuitement.",
 related=[R["roller"], R["honey"], R["vs"]]),

dict(slug="blinds-for-condos-and-apartments.html", type="advice", crumb="Stores pour condos", read=6, image=IMG["condo"],
 alt="Un salon de condo contemporain avec des fenêtres du plancher au plafond",
 title="Les meilleurs stores pour condos et appartements à Montréal (intimité, grandes vitres, règlements)",
 description="Les meilleurs stores pour les condos et appartements montréalais : intimité avec des voisins proches, fenêtres du plancher au plafond et larges, éblouissement sur les écrans, chaleur, règlements de syndicat et locations. Sur mesure et installés gratuitement.",
 og="Grandes vitres, voisins proches, règlements de copropriété — comment obtenir l’intimité sans perdre la vue.",
 h1="Les meilleurs stores pour condos et appartements : l’intimité sans perdre la <em>vue.</em>",
 lede="Vivre en condo à Montréal, c’est beaucoup de vitres, des voisins à quelques mètres, le soleil sur le sofa à 16 h — et un syndicat qui a son mot à dire sur ce qui se voit de l’extérieur. Voici comment régler tout ça.",
 body="""
        <h2>Les problèmes du condo, et ce qui les règle</h2>
        <h3>Voisins proches → l’intimité sans se plonger dans le noir</h3>
        <p>Les <a href="day-and-night-zebra-blinds.html"><strong>stores jour et nuit (zébrés)</strong></a> sont le héros du condo : alignez les bandes opaques pour l’intimité, les voiles pour la vue, d’un seul mouvement. Un rideau voile sur rail est l’alternative plus douce. Pour les chambres, un store occultant — voir plus bas.</p>
        <h3>Fenêtres du plancher au plafond et très larges</h3>
        <p>Les <strong>stores enrouleurs et zébrés</strong> gèrent proprement les grandes largeurs, et les <strong>rideaux sur rail au plafond</strong> sont superbes sur de hautes vitres. La motorisation en vaut la peine ici — ce sont des stores lourds à hisser plusieurs fois par jour. Les stores bateau deviennent lourds au-delà d’environ 2 m, alors on les divise ou on vous oriente ailleurs.</p>
        <h3>Soleil et chaleur</h3>
        <p>Les condos orientés à l’ouest et au sud cuisent l’été. Les <strong>toiles solaires/réfléchissantes pour enrouleurs</strong> coupent la chaleur et l’éblouissement tout en gardant la vue ; l’<a href="honeycomb-blinds.html"><strong>alvéolaire</strong></a> isole contre la chaleur estivale et le froid hivernal ; les <a href="outdoor-blinds.html"><strong>stores extérieurs</strong></a> sur un balcon sont les plus efficaces de tous (si les règlements le permettent).</p>
        <h3>Écrans et éblouissement</h3>
        <p>Vous travaillez de la maison ? Un enrouleur tamisant ou un store zébré sur la fenêtre du bureau garde l’éblouissement hors de l’écran sans bloquer la lumière du jour.</p>
        <h3>Dormir dans une ville lumineuse</h3>
        <p>Lampadaires, lumières des voisins, soleil hâtif : un <a href="blackout-blinds.html"><strong>store occultant avec rails latéraux</strong></a> dans la chambre. Vitre froide ? Alvéolaire occultant.</p>

        <h2>Règlements, syndicats et locations</h2>
        <ul>
          <li><strong>Les règles d’« apparence extérieure uniforme »</strong> sont courantes — beaucoup d’immeubles exigent du blanc ou du blanc cassé du côté rue. La plupart de nos tissus ont un endos neutre, donc vous pouvez avoir de la couleur à l’intérieur et du blanc à l’extérieur ; on vérifie vos règlements avec vous.</li>
          <li><strong>Les installations extérieures</strong> (stores extérieurs) exigent généralement une approbation — on peut vous aider à la présenter.</li>
          <li><strong>Vous louez ?</strong> Tout ce que nous installons s’enlève proprement ; les poses intérieures ne laissent que de petits trous de vis dans le cadre. Des options à tension et sans perçage existent pour certaines fenêtres — demandez-nous.</li>
        </ul>

        <h2>Nos choix condo</h2>
        <ul>
          <li><strong>Salon :</strong> stores zébrés (ou rideaux voile sur rail), motorisés si la vitre est grande.</li>
          <li><strong>Chambre :</strong> enrouleur ou alvéolaire occultant avec rails latéraux — sans cordon ou motorisé.</li>
          <li><strong>Bureau à domicile :</strong> enrouleur tamisant ou zébré.</li>
          <li><strong>Porte de balcon :</strong> un enrouleur/zébré large ou un rail de rideaux.</li>
          <li><strong>Le balcon lui-même :</strong> stores extérieurs, si le syndicat est d’accord.</li>
        </ul>
        <div class="callout"><strong>Spécifique à Montréal</strong><p>Beaucoup de tours du centre-ville et de Griffintown ont de très hautes vitres et des règles de façade strictes. Nous installons dans ces immeubles constamment — apportez-nous vos règlements et nous choisirons des tissus qui satisfont le syndicat <em>et</em> vous.</p></div>""",
 pros=None, cons=None, glance=None, body2="",
 faq=[("Quels stores conviennent le mieux à un condo avec de grandes fenêtres ?", "Zébrés (jour et nuit) ou enrouleurs pour les grandes largeurs, rideaux sur rail au plafond pour les hautes vitres — et la motorisation, parce que les gros stores sont lourds à manœuvrer au quotidien."),
      ("Comment obtenir l’intimité sans bloquer la vue ?", "Stores zébrés : alignez les bandes opaques pour l’intimité, les voiles pour la vue. Ou un rideau voile le jour avec un store ou une draperie la nuit."),
      ("Mon immeuble exige du blanc de l’extérieur — puis-je quand même avoir de la couleur ?", "Généralement oui. La plupart de nos tissus ont un endos neutre (blanc/blanc cassé), donc vous obtenez de la couleur à l’intérieur et un look uniforme à l’extérieur. On vérifie vos règlements."),
      ("Puis-je installer des stores dans une location ?", "Oui — les poses intérieures ne laissent que de petits trous de vis, et des options sans perçage existent pour certaines fenêtres. Demandez-nous."),
      ("Installez-vous dans les tours de condos ?", "Oui — partout à Montréal, y compris dans les immeubles aux règles de façade strictes et aux très hautes vitres. L’installation est gratuite.")],
 aside_h="Des conseils qui connaissent le condo", aside_p="Consultation gratuite à domicile. Apportez vos règlements — nous recommanderons des stores qui conviennent à vos vitres, vos voisins et votre syndicat.",
 cta_h="Grandes vitres, voisins proches, <em>réglé.</em>", cta_p="Réservez une consultation gratuite. Nous mesurons, vérifions les règles de votre immeuble et installons gratuitement.",
 related=[R["zebra"], R["blackout"], R["outdoor"]]),
]
